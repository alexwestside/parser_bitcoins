
from init import *

import requests
import json
import init

def get_coins_list():
    request = requests.get(init.api_coins)
    data_coins = request.content
    data_coins = json.loads(data_coins)
    data_coins = data_coins.get('Data')
    for coin in data_coins:
        if int(data_coins[coin].get('SortOrder')) in range(1, init.top):
            init.coins_list.append((data_coins[coin].get('Name')))
    print(init.coins_list)
