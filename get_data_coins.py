

import requests
import json
import re

api_data = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=BTC&tsym=USD'

currency_list = {u'DGB': ['BTC', 'ETH', 'LTC', 'DOGE'], u'ZEC': ['BTC', 'USD', 'CNY', 'ETH', 'EUR', 'XMR', 'RUB', 'NZDT', 'USDT', 'LTC', 'DOGE']}

def get_data_coins():
    for coin in currency_list:
        currencys = currency_list.get(coin)
        for currecy in currencys:
            re_find_coin = re.findall(r'(?<=\=)\w+(?=\&)', api_data)
            get_api_currency = api_data.replace(re_find_coin[0], str(coin))
            re_find_currency = re.findall(r'(?<=\=)\w+', get_api_currency)
            get_api_currency = get_api_currency.replace(re_find_currency[1], str(currecy))
            request = requests.get(get_api_currency)
            data_coin = request.content
            data_coin = json.loads(data_coin)
            data_coin = data_coin.get('Data')
            data_coin = data_coin.get('Exchanges')

get_data_coins()