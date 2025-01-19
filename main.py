import logging
from fastapi import FastAPI
from routers import game, shop
from cfg.logger import logger
from telegram_utils import send_telegram_message

uvicorn_logger = logging.getLogger("uvicorn")
uvicorn_logger.setLevel(logging.DEBUG)
uvicorn_logger.addHandler(logging.StreamHandler())

app = FastAPI(title="ULA777")
logger.info("APP STARTED")

@app.on_event("startup")
def startup_event():
    try:
        send_telegram_message("Service 'ULA777' has started!")
        logger.info("Startup event: Telegram notification sent.")
    except Exception as e:
        logger.error(f"Failed to send startup message: {e}")

@app.on_event("shutdown")
def shutdown_event():

    try:
        send_telegram_message(" Service 'ULA777' has stopped!")
        logger.info("Shutdown event: Telegram notification sent.")
    except Exception as e:
        logger.error(f"Failed to send shutdown message: {e}")

# Include routers
app.include_router(game.router, prefix="/game", tags=["Game"])
app.include_router(shop.router, prefix="/shop", tags=["Shop"])
