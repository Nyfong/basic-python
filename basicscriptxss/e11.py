import requests

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"

def get_updates():
    r = requests.get(BASE_URL + "getUpdates")
    return r.json()

def send_message(chat_id, text):
    requests.post(BASE_URL + "sendMessage", data={"chat_id": chat_id, "text": text})

# Run bot
updates = get_updates()
for update in updates["result"]:
    chat_id = update["message"]["chat"]["id"]
    user_msg = update["message"]["text"]
    send_message(chat_id, f"You said: {user_msg}")
