import random
import json
from fastapi import HTTPException

def load_users():
    try:
        with open('data/users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_users(users):
    with open('data/users.json', 'w') as file:
        json.dump(users, file, indent=4)

def play_game_logic(user_name: str, bet_number: int, bet_amount: int):
    if bet_number < 0 or bet_number > 100:
        raise HTTPException(status_code=400, detail="Bet number must be between 0 and 100")

    users = load_users()
    user = next((u for u in users if u["name"] == user_name), None)

    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    if user["balance"] < bet_amount:
        raise HTTPException(status_code=400, detail="Not enough balance to play")

    user["balance"] -= bet_amount
    roulette_number = random.randint(1, 100)

    if roulette_number == bet_number:
        winning = bet_amount * 2
        user["balance"] += winning
        save_users(users)
        return {"success": True, "message": f"You won! Your new balance is {user['balance']}"}

    save_users(users)
    return {"success": True, "message": f"You lost! Your new balance is {user['balance']}"}
