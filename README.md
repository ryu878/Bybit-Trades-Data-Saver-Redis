# Bybit Trades Data Saver Redis
Python script - Bybit Trades Data Saver using Redis in-memory key value database

Script will take the Trades data from Bybit REST API, save it to Redis in JSON format.

[![Latest release](https://badgen.net/github/release/Naereen/Strapdown.js)](https://aadresearch.xyz)

## Disclaimer
<hr>
This project is for informational purposes only. You should not construe this information or any other material as legal, tax, investment, financial or other advice. Nothing contained herein constitutes a solicitation, recommendation, endorsement or offer by us or any third party provider to buy or sell any securities or other financial instruments in this or any other jurisdiction in which such solicitation or offer would be unlawful under the securities laws of such jurisdiction.

If you intend to use real money, use it at your own risk.

Under no circumstances will we be responsible or liable for any claims, damages, losses, expenses, costs or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.
<hr>

## Install

Install Docker and Redis:

<code>sudo snap install docker</code>

<code>pip install redis</code>

<code>docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest</code>
   

To run the script type:

<code>python3 savedata_redis.py</code>

To open Redis database go to:

<code>http://localhost:8001</code>


## Contacts
Feel free to contact me via Discord: https://discord.gg/zSw58e9Uvf

or telegram: https://t.me/aadresearch

<a href="https://discord.gg/zSw58e9Uvf">![image](https://user-images.githubusercontent.com/81808867/166115186-70de12b2-39fd-4eda-bb12-c1d8bec24ac6.png)</a>

To start trading on Bybit please register here: [https://bybit.com](https://www.bybit.com/en-US/invite?ref=P11NJW)<br>
On Binance here: [https://binance.com](https://www.binance.com/en/activity/referral-entry/CPA?fromActivityPage=true&ref=CPA_00T5P4X8R6)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
