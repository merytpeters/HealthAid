#!/usr/bin/env python3
""""Health Inventory Routes"""
from flask import Blueprint, request, jsonify
from app.models.healthInventory import HealthInventory
<<<<<<< HEAD
from app.utils.crud import CRUD
=======
from datetime import date
>>>>>>> 42bb57cb70f68328bfb4a8d793b74340add6bde7


# Blueprint for inventory routes
inventory_bp = Blueprint('inventory', __name__)


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
        items = inventory.view_inventory(search_term=search_term)

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
def add_item():
    """Route to add item"""
    try:
        item_data = request.json
        required_fields = ['drug_name', 'quantity', 'unit', 'expiry_date']
        for field in required_fields:
            if field not in item_data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        inventory = HealthInventory()
        added_item = inventory.add_item(**item_data)
        return jsonify(added_item.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@inventory_bp.route('/<item_id>/restock', methods=['PUT'])
def restock(item_id):
    """Restock item route"""
    try:
        inventory = HealthInventory()
        restocked_item = inventory.restock(item_id)
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
        inventory = HealthInventory()
        deleted_item = inventory.delete_item(item_id)
        return jsonify({"message": f"Item {item_id} deleted successfully"}), 200
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
