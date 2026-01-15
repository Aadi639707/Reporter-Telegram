import os, time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- Config (Render Dashboard par ye keys zaroor dalein) ---
API_ID = int(os.environ.get("API_ID", "12345"))
API_HASH = os.environ.get("API_HASH", "your_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_token")

app = Client("reporter_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

BANNER = """
           REPORTER     SpiDer    TELEGRAM
    (Bot is running 24/7 on Render)
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("1️⃣ Reporter Channel", callback_data="rep_1")],
        [InlineKeyboardButton("2️⃣ Reporter Account", callback_data="rep_2")],
        [InlineKeyboardButton("3️⃣ Reporter Group (Update)", callback_data="rep_3")]
    ])
    await message.reply_text(f"```{BANNER}```\n\nChoose an option:", reply_markup=buttons)

@app.on_callback_query()
async def handle_buttons(client, callback_query):
    data = callback_query.data
    
    if data == "rep_1":
        await callback_query.answer("Starting Channel Reporter...")
        os.system("python report/reporter.py") # Same as your old code
        
    elif data == "rep_2":
        await callback_query.answer("Starting Account Reporter...")
        os.system("python report/report.py") # Same as your old code
        
    elif data == "rep_3":
        await callback_query.message.reply_text("This section is being updated.")

print("Bot is started successfully!")
app.run()
