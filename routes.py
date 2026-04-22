from flask import Blueprint, request, jsonify
import requests
from models import inventory, find_item

inventory_routes = Blueprint("inventory_routes", __name__)

@inventory_routes.route("/external/<barcode>")
def get_external_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        res = requests.get(url, headers=headers, timeout=5)

        if res.status_code != 200:
            return jsonify({
                "error": "External API request failed",
                "status_code": res.status_code
            }), 500

        data = res.json()

        if data.get("status") == 1:
            product = data["product"]
            return jsonify({
                "name": product.get("product_name"),
                "brand": product.get("brands"),
                "category": product.get("categories")
            })

        return jsonify({"error": "Product not found"}), 404

    except Exception as e:
        return jsonify({
            "error": "Request failed",
            "details": str(e)
        }), 500