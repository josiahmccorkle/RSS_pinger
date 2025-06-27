import time
import requests
import feedparser
from email_sender import sendEmail
import rss_constants
import secrets_file
from email.mime.text import MIMEText

def fetch_rss_feed(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        feed = feedparser.parse(response.text)
        print(f"Fetched {len(feed.entries)} entries from {url}")
        emailBody = ''

        for entry in feed.entries:
            emailBody += f"{entry.title}\n{entry.link}\n\n"

            msg = MIMEText(emailBody)
            msg["Subject"] = secrets_file.EMAIL_SUBJECT
            msg["From"] = secrets_file.EMAIL_ADDRESS
            msg["To"] = secrets_file.EMAIL_ADDRESS

        sendEmail(msg)
    except requests.RequestException as e:
        print(f"Error fetching RSS feed: {e}")

RSS_FEED_URL = rss_constants.CAREERS_FEED
fetch_rss_feed(RSS_FEED_URL)
