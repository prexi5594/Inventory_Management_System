inventory = []

def find_item(item_id):
    return next((item for item in inventory if item["id"] == item_id), None)