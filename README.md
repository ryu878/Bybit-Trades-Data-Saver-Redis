# Bybit Trades Data Saver Redis
Python script - Bybit Trades Data Saver using Redis in-memory key value database

Script will take the Trades data from Bybit API (websockets), save it to Redis in JSON format.

[![Latest release](https://badgen.net/github/release/Naereen/Strapdown.js)](https://aadresearch.xyz)

## Install

Install Docker and Redis:

<code>sudo apt install docker.io</code>

<code>pip install redis</code>

<code>docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest</code>

<code>pip install pybit==2.4.1</code>
   

To run the script type:

<code>python3 savedata_redis.py</code>

To open Redis database go to:

<code>http://localhost:8001</code>


## Disclaimer
This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial or other advice. Nothing contained here is a recommendation, endorsement or offer by me to buy or sell any securities or other financial instruments. If you intend to use real money, use it at your own risk. Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.

## Contacts
I develop trading bots of any complexity, dashboards and indicators for crypto exchanges, forex and stocks.
To contact me:

Discord: https://discord.gg/zSw58e9Uvf

Telegram: https://t.me/aadresearch

## VPS for bots and scripts
I prefer using DigitalOcean. 

To get $200 in credit over 60 days use my ref link: https://m.do.co/c/3d7f6e57bc04
