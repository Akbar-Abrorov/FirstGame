import json
from cfg.logger import logger


def load_users():
    with open('data/users.json', 'r') as file:
        return json.load(file)

#SAVE_USER
def save_users(users):
    with open('data/users.json', 'w') as file:
        json.dump(users, file, indent=4)


def load_items():
    with open('data/items.json', 'r') as file:
        data = json.load(file)
        logger.info(data)
        logger.info("This is an info message")
        logger.error("This is an error message")
        return data


def buy_item(user_name: int, item_name: int):
    items = load_items()
    users = load_users()

    user = next((u for u in users if u["name"] == user_name), None)
    if not user:
        return {"success": False, "message": "User not found"}

    item = next((i for i in items if i["name"].lower() == item_name.lower()), None)
    if not item:
        return {"success": False, "message": "Item not found"}
    if user["balance"] < item["price"]:
        return {"success": False, "message": "Not enough money to buy this item"}

    user["balance"] -= item["price"]
    user["items"][item_name] = user["items"].get(item_name, 0) + 1
    save_users(users)

    return {"success": True, "message": f"You bought {item['name']}", "new_balance": user["balance"]}
