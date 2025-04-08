# RSS Pinger

RSS Pinger is a Python script that fetches RSS feed entries from a specified URL, processes them, and sends the entries via email. This project is designed to periodically check for updates in an RSS feed and notify the user via email.

## Features

- Fetches RSS feed entries from a specified URL.
- Sends the feed entries via email using Gmail's SMTP server.
  - I may try to find a way to add other protocols as an option
- Configurable delay interval between feed fetches.
    - I may add a way to configure the intervals from a UI.  

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `requests`
  - `feedparser`
  - `smtplib`
  - `email`

## Installation

1. Clone this repository to your local machine.
2. Install the required Python libraries using pip:
   ```bash
   pip install requests feedparser


## Configuration
1. Update the RSS feed URL and delay interval in rss_constants.py:
```
CAREERS_FEED = "https://www.mozilla.org/en-US/careers/feed/"
DELAY_INTERVAL = 3600 * 3  # Fetch every 3 hours
```

```
GMAIL_PASSWORD = "your-gmail-app-password"
EMAIL_ADDRESS = "your-email@gmail.com"
```


## Usage
Run the script using Python:
`python RSS_pinger.py`


## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer
This script uses Gmail's SMTP server for sending emails. Ensure that you follow Gmail's security guidelines and use an App Password for authentication. Do not share your credentials publicly.
