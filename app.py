hereimport requests
import time

BOT_TOKEN = "8493314277:AAGno2KJcL1MuG_96hXkniQSa-lIhDCO0Lk"
CHAT_ID = "8185825710"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Message sent successfully!")
    else:
        print("❌ Failed to send message:", response.text)

def generate_signal():
    # Placeholder for real logic — replace later with AI/trading model
    return "BUY XAUUSD NOW 📈"

while True:
    signal = generate_signal()
    send_message(signal)
    time.sleep(60)
