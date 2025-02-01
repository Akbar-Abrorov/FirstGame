import logging
import sys
from cfg.tg_logger import TelegramLogHandler

logger = logging.getLogger("ULA777")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)
telegram_handler = TelegramLogHandler()
telegram_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.addHandler(telegram_handler)
