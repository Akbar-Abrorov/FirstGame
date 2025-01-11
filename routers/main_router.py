from fastapi import APIRouter

router = APIRouter()
@router.get('/')
def get_roots():
    return {"message": "Welcome to ULA777! Explore /game or /shop APIs"}