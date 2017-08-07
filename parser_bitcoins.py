import requests
import json
import re

url1 = 'https://www.cryptocompare.com/coins/btc/markets/USD'
url2 = 'https://www.cryptocompare.com/coins/eth/markets/BTC'

top = 20

coins_list = []
api_coins = 'https://www.cryptocompare.com/api/data/coinlist/'

currency_list = {}
api_currency = 'https://min-api.cryptocompare.com/data/top/pairs?fsym=XMR&limit=1000'

api_data = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=BTC&tsym=USD'
data_coins = []


def get_coins_list():
    request = requests.get(api_coins)
    data_coins = request.content
    data_coins = json.loads(data_coins)
    data_coins = data_coins.get('Data')
    for coin in data_coins:
        if int(data_coins[coin].get('SortOrder')) in range(1, top):
            coins_list.append((data_coins[coin].get('Name')))
    # print(coins_list)
    return

def get_currency_list():
    for coin in coins_list:
        re_find = re.findall(r'(?<=\=)\w+(?=\&)', api_currency)
        get_api_currency = api_currency.replace(re_find[0], str(coin) )
        request = requests.get(get_api_currency)
        data_currency = request.content
        data_currency = json.loads(data_currency)
        data_currency = data_currency.get('Data')
        for tok in data_currency:
            if coin not in currency_list:
                currency_list[coin] = []
                currency_list.get(coin).append(str(tok.get('toSymbol')))
            else:
                currency_list.get(coin).append(str(tok.get('toSymbol')))
        # print(currency_list)
    return

def get_data_coins():

    pass

get_coins_list()
get_currency_list()
get_data_coins()