from fastapi import APIRouter, HTTPException
from services.game_logic import play_game

router = APIRouter()


@router.post("/play", summary="PLay the Roulette game")
def play(user_name: str, bet_number: int, bet_amount:int):
    if bet_number < 0 or bet_number > 100:
        raise HTTPException(status_code=400, detail="Bet number must be between 0 and 100")
    result = play_game(user_name, bet_number, bet_amount)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])

    return result
