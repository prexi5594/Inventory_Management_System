import requests

BASE = "http://127.0.0.1:5000"

def view_items():
    try:
        res = requests.get(f"{BASE}/items")

        if res.status_code == 200:
            print(res.json())
        else:
            print("Error:", res.status_code, res.text)

    except Exception as e:
        print("Server not running or error:", e)


def add_item():
    item = {
        "id": int(input("ID: ")),
        "name": input("Name: "),
        "quantity": int(input("Quantity: "))
    }

    res = requests.post(f"{BASE}/items", json=item)
    print(res.json())


def delete_item():
    item_id = input("ID to delete: ")
    res = requests.delete(f"{BASE}/items/{item_id}")
    print(res.json())


def external():
    barcode = input("Barcode: ")
    res = requests.get(f"{BASE}/external/{barcode}")
    print(res.json())


while True:
    print("\n1.View 2.Add 3.Delete 4.External 5.Exit")
    choice = input("> ")

    if choice == "1":
        view_items()
    elif choice == "2":
        add_item()
    elif choice == "3":
        delete_item()
    elif choice == "4":
        external()
    else:
        break