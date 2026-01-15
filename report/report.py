import os, time, sys, platform
from telethon.sync import TelegramClient
from telethon.tl import types
from telethon import functions

# Colors & Utility Functions
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k, g = '\033[00;36m', '\033[90m', '\033[38;5;130m'

class TelegramReporter:
    def __init__(self, target_id, method="1", count=5):
        # Render Environment Variables se details uthana
        self.api_id = os.environ.get("USER_API_ID") 
        self.api_hash = os.environ.get("USER_API_HASH")
        self.phone_number = os.environ.get("USER_PHONE")
        self.password = os.environ.get("USER_PASSWORD") # Optional
        
        # Command arguments se details uthana
        self.scammer_id = target_id
        self.method = str(method)
        self.number = int(count)

    def report_spam(self):
        # Session file create karne ke liye Render ka writable path
        session_path = '/opt/render/project/src/reporter_session'
        
        with TelegramClient(session_path, self.api_id, self.api_hash) as client:
            # Agar first time login hai toh ye block ho sakta hai
            # 24/7 bot ke liye aapko session string use karni chahiye
            client.start(self.phone_number, self.password)

            try:
                user = client.get_entity(self.scammer_id)
                scammer_input_peer = types.InputPeerUser(user_id=user.id, access_hash=user.access_hash)
            except Exception as e:
                print(f'Error: {e}')
                return

            reasons = {
                "1": types.InputReportReasonSpam(),
                "2": types.InputReportReasonPornography(),
                "3": types.InputReportReasonViolence(),
                "4": types.InputReportReasonChildAbuse(),
                "7": types.InputReportReasonFake(),
                "9": types.InputReportReasonIllegalDrugs(),
                "10": types.InputReportReasonPersonalDetails()
            }

            reason = reasons.get(self.method, types.InputReportReasonOther())
            
            for i in range(1, self.number + 1):
                try:
                    client(functions.account.ReportPeerRequest(
                        peer=scammer_input_peer,
                        reason=reason,
                        message='Automated Report for Education Purpose'
                    ))
                    print(f"Report {i} sent to {self.scammer_id}")
                    time.sleep(1) # Flood wait se bachne ke liye
                except Exception as e:
                    print(f"Failed to send report {i}: {e}")
                    break

# Command Line Execute Logic
if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1] # Command line se target lena
        method = sys.argv[2] if len(sys.argv) > 2 else "1"
        count = sys.argv[3] if len(sys.argv) > 3 else "5"
        
        reporter = TelegramReporter(target, method, count)
        reporter.report_spam()
		
