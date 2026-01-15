import os
import time
from threading import Thread
from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- 1. FAKE SERVER FOR RENDER (Port Error Fix) ---
web = Flask('')

@web.route('/')
def home():
    return "Bot is alive and running 24/7!"

def run_web():
    # Render default port 10000 use karta hai
    port = int(os.environ.get("PORT", 10000))
    web.run(host='0.0.0.0', port=port)

# --- 2. BOT CONFIGURATION ---
# Render ke Environment Variables mein ye values zaroor dalein
API_ID = int(os.environ.get("API_ID", "1234567")) # Apna API ID dalein
API_HASH = os.environ.get("API_HASH", "your_api_hash_here")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token_here")

app = Client("reporter_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

BANNER = """
           REPORTER     SpiDer    TELEGRAM
    (Bot is running 24/7 on Render)
"""

# --- 3. BOT COMMANDS ---
@app.on_message(filters.command("start"))
async def start(client, message):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("1️⃣ Reporter Channel", callback_data="rep_1")],
        [InlineKeyboardButton("2️⃣ Reporter Account", callback_data="rep_2")],
        [InlineKeyboardButton("3️⃣ Reporter Group (Update)", callback_data="rep_3")]
    ])
    await message.reply_text(
        f"```{BANNER}```\n\n**🕷 Welcome to Spider Reporter Bot**\n\nNiche diye gaye buttons ka use karein:",
        reply_markup=buttons
    )

@app.on_callback_query()
async def handle_buttons(client, callback_query):
    data = callback_query.data
    
    if data == "rep_1":
        await callback_query.answer("Starting Channel Reporter...", show_alert=True)
        # Agar report/reporter.py file hai toh ye command chalegi
        os.system("python3 report/reporter.py")
        
    elif data == "rep_2":
        await callback_query.answer("Starting Account Reporter...", show_alert=True)
        os.system("python3 report/report.py")
        
    elif data == "rep_3":
        await callback_query.message.reply_text("⚠️ This section is being updated and will be added soon.")

# --- 4. EXECUTION ---
if __name__ == "__main__":
    # Pehle web server ko thread mein chalayein
    t = Thread(target=run_web)
    t.start()
    
    # Ab bot ko start karein
    print("Starting Bot...")
    app.run()
           
