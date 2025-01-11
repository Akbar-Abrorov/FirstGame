from logtail import LogtailHandler
import logging, sys

token = "xJUgQFKLFgasycR27PPF6uik"

logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('app.log')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

better_stack_handler = LogtailHandler(source_token=token)

logger.handlers = [stream_handler, file_handler,better_stack_handler]

logger.setLevel(logging.INFO)
