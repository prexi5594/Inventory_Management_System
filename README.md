# Inventory Management System (Flask API)

##  Project Description
This project is a Flask-based REST API for managing inventory in a retail system. It supports CRUD operations, integrates with an external API, and includes a CLI interface.

---

##  Features
- Create, Read, Update, Delete inventory items
- External API integration (OpenFoodFacts)
- CLI interface for interacting with the API
- Unit testing

---

##  Technologies Used
- Python
- Flask
- Requests
- Git & GitHub

---

## ▶How to Run

### 1. Install dependencies
```bash
pip install flask requests

flask routes
Endpoint                               Methods  Rule
-------------------------------------  -------  -----------------------
home                                   GET      /
inventory_routes.add_item              POST     /items
inventory_routes.delete_item           DELETE   /items/<int:item_id>
inventory_routes.get_external_product  GET      /external/<barcode>
inventory_routes.get_items             GET      /items
inventory_routes.update_item           PATCH    /items/<int:item_id>
static                                 GET      /static/<path:filename>