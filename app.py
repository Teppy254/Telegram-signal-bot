import requests
import time
import random

BOT_TOKEN = "8493314277:AAGno2KJcL1MuG_96hXkniQSa-lIhDCO0Lk"
CHAT_ID = "8185825710"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        response = requests.post(url, json=payload, timeout=10)
        print("Telegram response:", response.text)
        if response.status_code == 200:
            print("✅ Message sent successfully!")
        else:
            print("❌ Failed to send message:", response.text)
    except Exception as e:
        print("⚠️ Error sending message:", e)

def get_signal():
    """
    Simulated prediction function.
    For demonstration, it randomly returns BUY or SELL.
    Later, replace this with your actual prediction logic.
    """
    return random.choice(["BUY", "SELL"])

def main():
    send_message("🚀 Bot is now live and connected successfully!")
    while True:
        signal = get_signal()
        message = f"📊 Prediction Alert: {signal}"
        send_message(message)
        time.sleep(60)  # Wait 60 seconds before next prediction

if __name__ == "__main__":
    main()￼Enter
