import requests
from flask import jsonify

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