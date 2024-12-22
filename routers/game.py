from fastapi import APIRouter
from services.game_logic import play_game_logic

router = APIRouter()

@router.post("/play", summary="Play the Roulette game")
def play(user_name: str, bet_number: int, bet_amount: int):
    return play_game_logic(user_name, bet_number, bet_amount)