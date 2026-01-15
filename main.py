import os
from threading import Thread
from flask import Flask
from pyrogram import Client, filters

# --- Render Port Fix ---
web = Flask('')
@web.route('/')
def home(): return "Bot is running!"

def run_web():
    web.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

# --- Bot Setup ---
API_ID = int(os.environ.get("API_ID", "12345"))
API_HASH = os.environ.get("API_HASH", "your_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_token")

app = Client("reporter_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "**🕷 Reporter Bot Active 🕷**\n\n"
        "Kisi ko report karne ke liye ye command likhein:\n"
        "`/report @username` ya `/report_ch @channelname`"
    )

# Jab aap likhenge: /report @username
@app.on_message(filters.command("report"))
async def report_user(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Gunahgaar ka username bhi likhein! Example: `/report @duffer`")
    
    target = message.text.split(None, 1)[1]
    await message.reply_text(f"🚀 {target} par report attack shuru ho raha hai...")
    
    # Bina input ke script chalane ke liye:
    # Hum script ko 'target' variable pass karenge
    os.system(f"python3 report/report.py --target {target}")
    
    await message.reply_text(f"✅ {target} par report complete!")

if __name__ == "__main__":
    Thread(target=run_web).start()
    app.run()
    
