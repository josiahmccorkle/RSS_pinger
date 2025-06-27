#!/bin/bash
cd /Users/josiahmccorkle/Development/python/RSS_pinger || exit
source venv/bin/activate
/usr/bin/env python RSS_pinger.py


# ┬ ┬ ┬ ┬ ┬
# │ │ │ │ │
# │ │ │ │ └── Day of week (0–6 or Sun–Sat)
# │ │ │ └──── Month (1–12)
# │ │ └────── Day of month (1–31)
# │ └──────── Hour (0–23)
# └────────── Minute (0–59)



# Runs at 7a, 3p, and 10p:
# 0 7,15,22 * * * /Users/josiahmccorkle/Development/python/RSS_pinger/cron_runner.sh >> /Users/josiahmccorkle/Development/python/RSS_pinger/logs/rss.log 2>&1

# Runs every 1 minute:
# */1 * * * * /Users/josiahmccorkle/Development/python/RSS_pinger/cron_runner.sh >> /Users/josiahmccorkle/Development/python/RSS_pinger/logs/rss.log 2>&1

