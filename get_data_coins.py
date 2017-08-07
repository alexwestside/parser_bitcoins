
import requests
import json
import re
import csv
import os
from decimal import Decimal

datacoins = []

csv_colums = ['Coin name', 'Market', 'Currency', 'Price', 'Open 24H', 'Range 24H']

api_data = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=BTC&tsym=USD'

currency_list = {u'DGB': ['BTC', 'ETH', 'LTC', 'DOGE'], u'ZEC': ['BTC', 'USD', 'CNY', 'ETH', 'EUR', 'XMR', 'RUB', 'NZDT', 'USDT', 'LTC', 'DOGE']}

def csv_writer(datacoins):
    with open('datacoins.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(csv_colums)
        csvwriter.writerow(datacoins)

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
            for data in data_coin:
                datacoins.append(data.get('FROMSYMBOL'))
                datacoins.append(data.get('MARKET'))
                datacoins.append(data.get('TOSYMBOL'))
                datacoins.append(data.get('PRICE'))
                datacoins.append(data.get('OPEN24HOUR'))
                if Decimal.from_float(float(data.get('HIGH24HOUR')) - float(data.get('LOW24HOUR'))) < 1.0E-5:
                    datacoins.append((str(Decimal.from_float(float(str((data.get('HIGH24HOUR')))))))[:10])
                else:
                    datacoins.append(str(Decimal.from_float(float(data.get('HIGH24HOUR')) - float(data.get('LOW24HOUR')))))
                csv_writer(datacoins)

get_data_coins()