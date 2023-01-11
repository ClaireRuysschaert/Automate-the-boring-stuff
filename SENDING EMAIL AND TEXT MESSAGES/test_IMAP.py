import os
# import pprint

import imapclient
from dotenv import load_dotenv
import pyzmail

# Connecting to server with a client object
imap_obj = imapclient.IMAPClient("imap.gmail.com", ssl=True)
# Logging
load_dotenv()
smtp_pw = os.getenv("smtp_password")
imap_obj.login("yukimargoulin@gmail.com", smtp_pw)

# Searching for Email
imap_obj.select_folder("INBOX", readonly=True)
# readonly=False if we want mails to get marked as read
UIDs = imap_obj.search("UNSEEN")
raw_message = imap_obj.fetch(UIDs, ["BODY[]"])  # RDC 822 format
# pprint.pprint(raw_message)
# Getting Email from raw message
message = pyzmail.PyzMessage.factory(raw_message[1][b'BODY[]'])
print(message.get_addresses('from'))
print(message.text_part.get_payload().decode(message.text_part.charset))
# print(message.html_part.get_payload().decode(message.html_part.charset))
imap_obj.logout()
