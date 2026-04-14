from flask import Blueprint, request, jsonify
import requests
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
        return jsonify({"error": "Not found"}), 404
    item.update(request.json)
    return jsonify(item)

@inventory_routes.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = find_item(item_id)
    if not item:
        return jsonify({"error": "Not found"}), 404
    inventory.remove(item)
    return jsonify({"message": "deleted"})

@inventory_routes.route("/external/<barcode>")
def get_external_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    res = requests.get(url).json()

    if res["status"] == 1:
        product = res["product"]
        return jsonify({
            "name": product.get("product_name"),
            "brand": product.get("brands"),
            "category": product.get("categories")
        })

    return jsonify({"error": "Product not found"}), 404