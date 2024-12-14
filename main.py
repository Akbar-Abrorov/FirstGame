from fastapi import FastAPI
from routers import game, shop


app = FastAPI(title="ULA777")


app.include_router(game.router, prefix="/game", tags=["Game"])
app.include_router(shop.router, prefix="/shop", tags=["Shop"])

@app.get('/')
def get_roots():
    return {"message": "Welcome to ULA777! Explore /game or /shop APIs"}