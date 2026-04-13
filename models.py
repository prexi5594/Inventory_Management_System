inventory = []

def find_item(item_id):
    return next((i for i in inventory if i["id"] == item_id), None)