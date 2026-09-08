import os, time, requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID", "")

def send_msg(text):
    if not BOT_TOKEN or not CHAT_ID: return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"})
    except: pass

if __name__ == "__main__":
    send_msg("✅ *Scanner Started on Render!* - Mahesh")
    while True:
        print("Scanner running...")
        time.sleep(60)
