# Ryuryu's Bybit Trades Saver
# Redis Edition (Production Mode #6973)
# --------------------------------------------------
# (c) 2023 Ryan Hayabusa 
# GitGub: https://github.com/ryu878
# Web: https://aadresearch.xyz
# Discord: ryuryu#4087
# --------------------------------------------------

import time
import json
import redis
from config import *
from pybit import usdt_perpetual
from inspect import currentframe



def get_linenumber():
    cf = currentframe()
    global line_number
    line_number = cf.f_back.f_lineno


ws_perp = usdt_perpetual.WebSocket(
    test=False,
    api_key=api_key,
    api_secret=api_secret,
    domain=domain
)


def get_trades(trades):
    print(trades)

    r = redis.Redis(host='localhost',port=6379,db=0)
    data_str = json.dumps(trades)

    print(trades)
    trade_id = trades['data'][0]['trade_id']
    # print(trade_id)
    expire = 60 * 30

    r.json().set(trade_id, '.', data_str)
    r.json().execute_command('expire', trade_id, expire_s)


ws_perp.trade_stream(get_trades, assets_50)


while True:

    time.sleep(1)
