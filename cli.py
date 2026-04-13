import requests

BASE = "http://127.0.0.1:5000"

def view_items():
    print(requests.get(f"{BASE}/items").json())

def add_item():
    data = {
        "id": int(input("ID: ")),
        "name": input("Name: "),
        "quantity": int(input("Qty: "))
    }
    print(requests.post(f"{BASE}/items", json=data).json())

while True:
    print("\n1.View 2.Add 3.Exit")
    choice = input("> ")

    if choice == "1":
        view_items()
    elif choice == "2":
        add_item()
    else:
        break