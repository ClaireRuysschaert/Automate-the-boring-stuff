import smtplib
from dotenv import load_dotenv
import os

# Connection to an SMTP mail server, TLS encryption
smtp_obj: smtplib.SMTP = smtplib.SMTP("smtp.gmail.com", 587)
print(type(smtp_obj))
# say hello to the server, 250
smtp_obj.ehlo()
# Encryption for connection, 220
smtp_obj.starttls()
# Logging in, 235
load_dotenv()
smtp_pw = os.getenv('smtp_password')
print(smtp_obj.login("yukimargoulin@gmail.com", smtp_pw))
smtp_obj.sendmail(
    "yukimargoulin@gmail.com",
    "netclaire@hotmail.fr",
    "Subject: Mew.\nDear mom, please give me more food. I'm getting skinnier "
    "by the time flies.\nMewe you. \nYuki"
)
smtp_obj.quit()
