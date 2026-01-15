import os
from threading import Thread
from flask import Flask
from pyrogram import Client, filters

# --- Render Port Fix (Bot ko online rakhne ke liye) ---
web = Flask('')

@web.route('/')
def home():
    return "Bot is running 24/7!"

def run_web():
    # Render default port 10000 use karta hai
    port = int(os.environ.get("PORT", 10000))
    web.run(host='0.0.0.0', port=port)

# --- Bot Configuration ---
# Details Render Environment Variables se uthayega
API_ID = int(os.environ.get("API_ID", "27070308"))
API_HASH = os.environ.get("API_HASH", "d1bfc4df9e7a49882cf91fc9f98fc8dd")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("reporter_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- Commands ---

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "**🕷 Reporter Bot Active 🕷**\n\n"
        "Kisi ID ko report karne ke liye ye command bhejें:\n"
        "`/report @username`"
    )

@app.on_message(filters.command("report"))
async def trigger_report(client, message):
    if len(message.command) < 2:
        return await message.reply_text("❌ Username missing! Example: `/report @duffer`")

    target = message.command[1]
    status_msg = await message.reply_text(f"🚀 **Process Shuru!**\n🎯 Target: {target}\n\nLogs check karein...")

    # Report script ko trigger karna aur logs ko console mein dikhana
    # Agar aapki file 'report' folder ke andar hai toh 'report/report.py' likhein
    # Agar bahar hai toh sirf 'report.py'
    exit_code = os.system(f"python3 report/report.py {target}")

    if exit_code == 0:
        await status_msg.edit_text(f"✅ **Process Complete!**\nTarget: {target}\nReports bhej di gayi hain.")
    else:
        await status_msg.edit_text(f"⚠️ **Script Run Hui!**\nLekin shayad koi error aaya hai. Render Logs check karein.")

# --- Start Everything ---
if __name__ == "__main__":
    # Web server ko alag thread mein chalana
    Thread(target=run_web).start()
    
    # Bot ko start karna
    print("Bot is starting...")
    app.run()
    
