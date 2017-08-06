
import requests
import json
import coins_list
import heapq

market_list = ['Bitfinex',
        'Poloniex'
        'GDAX',
        'Bitstamp',
        'Gemini',
        'Kraken',
        'BitTrex',
        'LakeBTC',
        'Gatecoin',
        'itBit',
        'HitBTC',
        'OKCoin',
        'Cexio',
        'Quoine',
        'Exmo',
        'LiveCoin',
        'LocalBitcoins',
        'Yobit',
        'Coinfloor',
        'QuadrigaCX',
        'WavesDEX',
        'BitBay',
        'TheRockTrading',
        'BitSquare']

api1 = 'https://min-api.cryptocompare.com/data/generateAvg?fsym=BTC&tsym=USD&markets='

for market in market_list:
        request = api1 + market
        response = requests.get(request)
        data_market = response.content
        data_market = json.loads(data_market)
        if data_market.get('RAW') is not None:
                price = data_market.get('RAW').get('PRICE')
                print (price)







