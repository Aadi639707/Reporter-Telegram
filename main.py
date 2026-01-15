import os
import time
import subprocess
from threading import Thread
from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- 1. RENDER PORT FIX (Flask Server) ---
web = Flask('')

@web.route('/')
def home():
    return "Bot is running 24/7!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.run(host='0.0.0.0', port=port)

# --- 2. BOT CONFIGURATION ---
API_ID = int(os.environ.get("API_ID", "12345"))
API_HASH = os.environ.get("API_HASH", "your_api_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token")

app = Client("reporter_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

BANNER = """
    🕷 REPORTER SpiDer TELEGRAM 🕷
    Status: Active (24/7)
"""

# --- 3. COMMANDS & HANDLERS ---

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        f"```{BANNER}```\n"
        "**Kaise use karein?**\n\n"
        "Report karne ke liye niche di gayi command bhejें:\n"
        "`/report @username method_number count` \n\n"
        "**Example:** `/report @duffer 1 10` \n"
        "(Iska matlab: @duffer ko Spam (1) ki 10 reports bhejo)"
    )

@app.on_message(filters.command("report"))
async def report_trigger(client, message):
    # Command check: /report @target method count
    if len(message.command) < 2:
        return await message.reply_text("❌ Username missing! \nFormat: `/report @username`")

    target = message.command[1]
    method = message.command[2] if len(message.command) > 2 else "1"
    count = message.command[3] if len(message.command) > 3 else "5"

    status_msg = await message.reply_text(f"🚀 **Report Process Started!**\n\n🎯 Target: {target}\n🔢 Method: {method}\n📊 Count: {count}")

    try:
        # report/report.py ko background mein run karna
        # Hum arguments pass kar rahe hain: target, method, count
        process = subprocess.Popen(
            ["python3", "report/report.py", target, method, count],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Script finish hone ka wait karna (Optional, agar response chahiye)
        await status_msg.edit_text(f"✅ **Report Sent Successfully!**\nTarget: {target} par kaam ho gaya.")
        
    except Exception as e:
        await status_msg.edit_text(f"❌ **Error:** {str(e)}")

# --- 4. STARTING EVERYTHING ---
if __name__ == "__main__":
    # Web server start karein (Render ke liye)
    Thread(target=run_web).start()
    
    # Bot start karein
    print("Bot is starting...")
    app.run()
    
