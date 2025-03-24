import time
import requests
import feedparser
import rss_constants

def fetch_rss_feed(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        feed = feedparser.parse(response.text)
        print(f"Fetched {len(feed.entries)} entries from {url}")
        for entry in feed.entries:
            print(f"Title: {entry.title}")
            print(f"Link: {entry.link}\n")
    except requests.RequestException as e:
        print(f"Error fetching RSS feed: {e}")

RSS_FEED_URL = rss_constants.CAREERS_FEED  # Replace with a valid RSS feed URL

while True:
    fetch_rss_feed(RSS_FEED_URL)
    time.sleep(rss_constants.DELAY_INTERVAL)  # Wait for one hour before fetching again
