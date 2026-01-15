import os, sys, time
from telethon import TelegramClient, types, functions
from telethon.sessions import StringSession

def start_report():
    target = sys.argv[1] if len(sys.argv) > 1 else None
    if not target: return
    
    # Render ke Environment Variables se String uthayega
    string_session = os.environ.get("SESSION_STRING")
    api_id = 27070308
    api_hash = 'd1bfc4df9e7a49882cf91fc9f98fc8dd'
    
    if not string_session:
        print("Error: SESSION_STRING not found in Render settings!")
        return

    with TelegramClient(StringSession(string_session), api_id, api_hash) as client:
        try:
            entity = client.get_entity(target)
            for i in range(10): # 10 reports bhejne ke liye
                client(functions.account.ReportPeerRequest(
                    peer=entity,
                    reason=types.InputReportReasonSpam(),
                    message='Reporting for spam/abuse'
                ))
                print(f"Report {i+1} sent!")
                time.sleep(2)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    start_report()
	
