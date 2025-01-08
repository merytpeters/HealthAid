#!/usr/bin/env python3
""""Health Inventory Routes"""
from flask import Blueprint, request, jsonify
from app.models.healthInventory import HealthInventory
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity


# Blueprint for inventory routes
inventory_bp = Blueprint('inventory', __name__)


@inventory_bp.before_request
@jwt_required()
def protect_inventory_routes():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({"error": "User not authenticated"}), 40

@inventory_bp.route('/', methods=['GET'])
def get_inventory():
    """Retrieve all items from in the inventory and specific item search too"""
    try:
        search_term = request.args.get('search', None)

        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))

        inventory = HealthInventory()
        items = inventory.view_inventory(search_term=search_term, page=page, per_page=per_page)

        items_list = [item.to_dict() for item in items]
        return jsonify(items_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@inventory_bp.route('/search', methods=['GET'])
def search():
    """Search inventory for item"""
    try:
        search_term = request.args.get('search', None)
        if not search_term:
            return jsonify({"error": "Search term is required"}), 400
        inventory = HealthInventory()
        items = []
        page = 1
        per_page = 10
        while True:
            paginated_items = inventory.view_inventory(search_term=search_term, page=page, per_page=per_page)
            if not paginated_items:
                break
            items.extend(paginated_items)
            page += 1

        items_list = [item.to_dict() for item in items]
        return jsonify(items_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@inventory_bp.route('/restock', methods=['GET'])
def search_items_due_for_restock():
    """Search for items that are due for restock"""
    try:
        today = date.today()
        inventory = HealthInventory()
        items = inventory.items_due_for_restock(today)
        items_list = [item.to_dict() for item in items]
        return jsonify(items_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@inventory_bp.route('/additem', methods=['POST'])
@jwt_required()
def add_item():
    """Route to add item"""
    try:
        item_data = request.json
        required_fields = ['drug_name', 'quantity', 'unit', 'expiry_date']
        for field in required_fields:
            if field not in item_data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        user_id = get_jwt_identity()
        if not user_id:
            return jsonify({"error": "User must be logged in"}), 401
        
        item_data['user_id'] = user_id

        inventory = HealthInventory()
        added_item = inventory.add_item(**item_data)
        if added_item is None:
            return jsonify({"error": "Failed to add item"}), 500
        return jsonify(added_item.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@inventory_bp.route('/restockitem', methods=['PUT'])
def restock():
    """Restock item route"""
    try:
        data = request.get_json()
        item_name = data.get('drug_name')
        quantity_to_add = data.get('quantity')
        if not item_name or not isinstance(item_name, str):
            return jsonify({"error": "Invalid item name"}), 400

        if not isinstance(quantity_to_add, int) or quantity_to_add <= 0:
            return jsonify({"error": "Invalid quantity"}), 400
        
        # Find the item by name
        item = HealthInventory.query.filter_by(drug_name=item_name).first()

        if not item:
            return jsonify({"error": "Item not found"}), 404

        # Restock the item
        restocked_item = item.restock(quantity_to_add)
        return jsonify(restocked_item.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@inventory_bp.route('/restock_notification', methods=['GET'])
def restock_notification():
    """Restock notification route"""
    try:
        item = HealthInventory.restock_notification()
        return jsonify(item), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@inventory_bp.route('/delete_item/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Delete item route"""
    try:
        data = request.get_json()
        item_name = data.get('drug_name') if data else None
        item = HealthInventory.query.get(item_id)
        if not item:
            return jsonify({"error": "Item not found"}), 404
        if item_name and item.drug_name != item_name:
            return jsonify({"error": "Item name mismatch"}), 400
        deleted_item = item.delete_item(item_id)
        return jsonify({"message": f"Item {deleted_item} deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@inventory_bp.route('/delete_expired', methods=['DELETE'])
def delete_expired_items():
    """Delete expired items route"""
    try:
        expired_param = request.args.get('expired')
        if not expired_param:
            return jsonify({"error": "Missing 'expired' parameter"}), 400
        
        inventory = HealthInventory()
        deleted_items = inventory.delete_expired_items(expired=expired_param)
        return jsonify({"message": f"{len(deleted_items)} expired items deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@inventory_bp.route('/delete', methods=['DELETE'])
def delete_inventory():
    """Delete all items in inventory"""
    try:
        inventory = HealthInventory()
        deleted_items = inventory.delete_item()
        return jsonify({"message": "All items deleted", "count": len(deleted_items)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
