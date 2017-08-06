
# api = 'https://min-api.cryptocompare.com/data/top/pairs?fsym=XMR&limit=1000'

from init import *


def get_currency_list():
    for coin in coins_list:
        get_api_currency = api_currency.replace(re.findall(r'(?<=(\=))\w+(?=(\&))', api_currency), coin)
        request = requests.get(get_api_currency)
        data_currency = request.content
        data_currency = json.loads(data_currency)
        data_currency = data_currency.get('Data')
        print(data_currency)