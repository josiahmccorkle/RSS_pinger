
from email.mime.text import MIMEText
import smtplib
import secrets_file

def sendEmail(msg):
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            # server.set_debuglevel(1)
            server.login(secrets_file.EMAIL_ADDRESS, secrets_file.GMAIL_PASSWORD)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")