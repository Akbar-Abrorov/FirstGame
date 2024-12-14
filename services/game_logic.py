import random
import json

def load_users():
    with open('data/users.json', 'r') as file:
        return json.load(file)



def save_users(users):
    with open('data/users.json', 'w') as file:
        json.dump(users, file, indent=4)



def play_game(user_name:str , bet_number: int, bet_amount: int):
    users = load_users()
    user = next((u for u in users if u["name"] == user_name), None)

    if not user:
        return {"success":False, "message": "User not found"}

    if user["balance"] < bet_amount:
        return {"success": False, "message": "Not enough balance to play "}

    user["balance"] -= bet_amount
    roulette_number = random.randint(0, 100)


    if roulette_number == bet_number:
        winning = bet_amount * 2
        user["balance"] += winning
        save_users(users)
        return {"success":True, "message": f"You won! Your new balance is {user['balance']}"}

    save_users(users)
    return {"success":True, "message": f"You lost! Your new balance is {user['balance']}"}
