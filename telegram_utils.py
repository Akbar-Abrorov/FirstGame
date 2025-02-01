import requests

BOT_TOKEN = "8018062200:AAEN79C5bbYdMUwujueoW4wxrrdKDYna7WE"
CHAT_ID = "-1002289192692"

def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        raise Exception(f"Failed to send message: {response.text}")
