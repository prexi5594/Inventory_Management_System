from flask import Blueprint, request, jsonify
import requests

inventory_routes = Blueprint("inventory_routes", __name__)

inventory = []

def find_item(item_id):
    return next((i for i in inventory if i["id"] == item_id), None)

# CREATE
@inventory_routes.route("/items", methods=["POST"])
def add_item():
    data = request.json
    inventory.append(data)
    return jsonify(data), 201

# READ
@inventory_routes.route("/items", methods=["GET"])
def get_items():
    return jsonify(inventory)

# UPDATE
@inventory_routes.route("/items/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    item = find_item(item_id)
    if not item:
        return {"error": "Not found"}, 404
    item.update(request.json)
    return jsonify(item)

# DELETE
@inventory_routes.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = find_item(item_id)
    if not item:
        return {"error": "Not found"}, 404
    inventory.remove(item)
    return {"message": "deleted"}

# EXTERNAL API
@inventory_routes.route("/external/<barcode>")
def get_external_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)

    data = res.json()

    if data.get("status") == 1:
        product = data["product"]
        return jsonify({
            "name": product.get("product_name"),
            "brand": product.get("brands"),
            "category": product.get("categories")
        })

    return jsonify({"error": "Product not found"}), 404