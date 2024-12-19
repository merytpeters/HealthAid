#!/usr/bin/env python3
""""Health Inventory Routes"""
from flask import Blueprint, request, jsonify
from models.healthInventory import HealthInventory
from utils.crud import CRUD


# Blueprint for inventory routes
inventory_bp = Blueprint('inventory', __name__)


@inventory_bp.route('/', methods=['GET'])
def get_inventory():
    """Retrieve all items from in the inventory"""
    try:
        search_term = request.args.get('search', None)

        items = HealthInventory.view_inventory(search_term=search_term)

        items_list = [item.to_dict() for item in items]
        return jsonify(items_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@inventory_bp.route('/search', methods=['GET'])
def search():
    """Search inventory"""
    pass

@inventory_bp.route('/?filter=restock', methods=['GET'])
def search_items_due_for_restock():
    pass

@inventory_bp.route('/additem', methods=['POST'])
def add_item():
    pass

@inventory_bp.route('/<item_id>/restock', methods=['PUT'])
def restock():
    pass

@inventory_bp.route('/restock_notification', methods=['GET'])
def restock_notofication():
    pass

@inventory_bp.route('/delete_item/<item_id>', methods=['DELETE'])
def delete_item():
    pass

@inventory_bp.route('/delete_expired', methods=['DELETE'])
def delete_expired_items():
    pass

@inventory_bp.route('/delete', methods=['DELETE'])
def delete_inventory():
    pass
