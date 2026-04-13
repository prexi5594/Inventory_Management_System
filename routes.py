from flask import Blueprint, request, jsonify
from models import inventory, find_item

inventory_routes = Blueprint("inventory_routes", __name__)

@inventory_routes.route("/items", methods=["POST"])
def add_item():
    data = request.json
    inventory.append(data)
    return jsonify(data), 201

@inventory_routes.route("/items", methods=["GET"])
def get_items():
    return jsonify(inventory)

@inventory_routes.route("/items/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    item = find_item(item_id)
    if not item:
        return {"error": "Not found"}, 404
    item.update(request.json)
    return jsonify(item)

@inventory_routes.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = find_item(item_id)
    inventory.remove(item)
    return {"message": "deleted"}