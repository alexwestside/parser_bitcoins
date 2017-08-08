import requests
import json
import re
import csv
from decimal import Decimal

top = 20 # Count of top coins that need to collect in dataset

coins_list = []
api_coins = 'https://www.cryptocompare.com/api/data/coinlist/' # Exemple of api request that given data of all coins wich we will range by parametr SortOrder

currency_list = {}
api_currency = 'https://min-api.cryptocompare.com/data/top/pairs?fsym=XMR&limit=1000' # Exemple of api request that given data of a coin-currency

data_coins = []
api_data = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=BTC&tsym=USD' # Exemple of api reauest that given data of a coin-market-currency

csv_colums = ['Coin name', 'Market', 'Currency', 'Price', 'Open 24H', 'Range 24H'] # Struct of CSV file

# Func making a list of a top20 coins
def get_coins_list():
    request = requests.get(api_coins)
    data_coins = request.content
    data_coins = json.loads(data_coins)
    data_coins = data_coins.get('Data')
    for coin in data_coins:
        if int(data_coins[coin].get('SortOrder')) in range(1, top):
            coins_list.append((data_coins[coin].get('Name')))
    return

# Func making a lists all curencys in connect by each coin
def get_currency_list():
    for coin in coins_list:
        re_find = re.findall(r'(?<=\=)\w+(?=\&)', api_currency)
        get_api_currency = api_currency.replace(re_find[0], str(coin))
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
    return

# Func making a dataset fo all coin in coins_list and write it in file
def get_data_coins():
    fp = open('datacoins.csv', 'wb')
    csvwriter = csv.writer(fp, delimiter=',')
    csvwriter.writerow(csv_colums)
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
            if len(data_coin) != int(0):
                data_coin = data_coin.get('Exchanges')
                for data in data_coin:
                    datacoins = []
                    datacoins.append(data.get('FROMSYMBOL'))
                    datacoins.append(data.get('MARKET'))
                    datacoins.append(data.get('TOSYMBOL'))
                    datacoins.append(str(Decimal(float(data.get('PRICE'))))[:10])
                    datacoins.append(str(Decimal(float(data.get('OPEN24HOUR'))))[:10])
                    datacoins.append(str(Decimal(float(data.get('HIGH24HOUR')) - float(data.get('LOW24HOUR'))))[:10])
                    csvwriter.writerow(datacoins)
    fp.close()
    return

# Main func produce dataset named - "datacoins.csv"
def main():
    get_coins_list()
    get_currency_list()
    get_data_coins()

if __name__ == "__main__":
    main()