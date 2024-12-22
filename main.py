import logging
from fastapi import FastAPI
from routers import game, shop, main_router

uvicorn_logger = logging.getLogger("uvicorn")
uvicorn_logger.setLevel(logging.DEBUG)
uvicorn_logger.addHandler(logging.StreamHandler())


app = FastAPI(title="ULA777")


app.include_router(game.router, prefix="/game", tags=["Game"])
app.include_router(shop.router, prefix="/shop", tags=["Shop"])
app.include_router(main_router.router, prefix="/main", tags=["Main"])