from fastapi import APIRouter, HTTPException
from services.shop_logic import load_items, buy_item

router = APIRouter()

@router.get("/items")
def get_items():
    return load_items()



@router.post("/buy")
def buy(user_name : str, item_name:str):
    result = buy_item(user_name, item_name)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result