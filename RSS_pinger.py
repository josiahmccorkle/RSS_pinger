import time
import requests
import feedparser
import rss_constants
import secrets_file
import smtplib
from email.mime.text import MIMEText

def fetch_rss_feed(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        feed = feedparser.parse(response.text)
        print(f"Fetched {len(feed.entries)} entries from {url}")
        emailBody = ''

        for entry in feed.entries:
            print(f"Title: {entry.title}")
            print(f"Link: {entry.link}\n")
            emailBody += f"{entry.title}\n{entry.link}\n\n"

        try:
            msg = MIMEText(emailBody)
            msg["Subject"] = "Mozilla Positions"
            msg["From"] = secrets_file.EMAIL_ADDRESS
            msg["To"] = secrets_file.EMAIL_ADDRESS

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                # server.set_debuglevel(1)
                print("logging in to email!")
                server.login(secrets_file.EMAIL_ADDRESS, secrets_file.GMAIL_PASSWORD)
                print("sending email!")
                server.send_message(msg)
                print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
    except requests.RequestException as e:
        print(f"Error fetching RSS feed: {e}")

RSS_FEED_URL = rss_constants.CAREERS_FEED  # Replace with a valid RSS feed URL

while True:
    fetch_rss_feed(RSS_FEED_URL)
    time.sleep(rss_constants.DELAY_INTERVAL)  # Wait for one hour before fetching again
