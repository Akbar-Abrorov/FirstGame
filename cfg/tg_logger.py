import logging
from telegram_utils import send_telegram_message

class TelegramLogHandler(logging.Handler):
    def emit(self, record):
        try:
            log_entry = self.format(record)
            send_telegram_message(log_entry)
        except Exception as e:
            print(f"Failed to send log to Telegram: {e}")

