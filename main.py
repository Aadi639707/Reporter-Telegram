import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- Credentials (Render ke Environment Variables mein set karein) ---
API_ID = int(os.environ.get("API_ID", "12345"))
API_HASH = os.environ.get("API_HASH", "your_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_token")

app = Client("reporter_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Start Command
@app.on_message(filters.command("start"))
async def start(client, message):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("1️⃣ Report Channel", callback_data="rep_ch")],
        [InlineKeyboardButton("2️⃣ Report Account", callback_data="rep_acc")],
        [InlineKeyboardButton("3️⃣ Report Group", callback_data="rep_grp")]
    ])
    
    await message.reply_text(
        "**🕷 Reporter Telegram Bot 🕷**\n\nNiche diye gaye buttons par click karke report shuru karein:",
        reply_markup=buttons
    )

# Button Click Handling
@app.on_callback_query()
async def callback(client, callback_query):
    data = callback_query.data
    
    if data == "rep_ch":
        await callback_query.message.edit_text("✅ Channel Report logic start ho raha hai...")
        # Yahan aap apna reporting ka logic (reporter.py wala) likh sakte hain
        
    elif data == "rep_acc":
        await callback_query.message.edit_text("✅ Account Report logic start ho raha hai...")
        
    elif data == "rep_grp":
        await callback_query.message.edit_text("⚠️ Ye section abhi update ho raha hai (Coming Soon).")

print("Bot is alive...")
app.run()
