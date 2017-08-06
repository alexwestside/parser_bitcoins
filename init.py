
import requests
import json
import init
import re


url1 = 'https://www.cryptocompare.com/coins/btc/markets/USD'
url2 = 'https://www.cryptocompare.com/coins/eth/markets/BTC'

top = 20

coins_list = []
api_coins = 'https://www.cryptocompare.com/api/data/coinlist/'

currency_list = {}
api_currency = 'https://min-api.cryptocompare.com/data/top/pairs?fsym=XMR&limit=1000'