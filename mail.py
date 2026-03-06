import smtplib
from email.mime.text import MIMEText
import os

def send_mail(content):
   sender = os.environ["EMAIL"]
   password = os.environ["EMAIL_PASSWORD"]
  
   msg = MIMEText(content)
   msg["Subject"] = "Daily Tech Trend"
   msg["From"] = sender
   msg["To"] = sender
  
   server = smtplib.SMTP_SSL("smtp.gmail.com",465)
  
   server.login(sender,password)
   server.send_message(msg)
  
   server.quit()
