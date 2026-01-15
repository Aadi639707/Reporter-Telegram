import os, sys, time
from telethon import TelegramClient, types, functions
from telethon.sessions import StringSession

# Target aur details lena
target = sys.argv[1] if len(sys.argv) > 1 else None
# Pehli ID check karna
string = os.environ.get("SESSION_1")

if not target or not string:
    print(f"Error: Target({target}) or Session({string}) missing!")
    sys.exit()

try:
    with TelegramClient(StringSession(string), 27070308, 'd1bfc4df9e7a49882cf91fc9f98fc8dd') as client:
        print(f"Connecting to ID for {target}...")
        entity = client.get_entity(target)
        client(functions.account.ReportPeerRequest(
            peer=entity,
            reason=types.InputReportReasonSpam(),
            message='Spamming'
        ))
        print("Report 1 sent!") # Ye line ab aani chahiye
except Exception as e:
    print(f"FAILED: {e}")
	
