
import csv
import os

dict = [{'Coin name': 'BTC', 'Market': 'PPP', 'Currency': 'USD', 'Price': '3251', 'Open 24H': '1253', 'Range 24H': '125'}]

list = ['BTC', 'PPP', 'USD', '3251', '1253', '125']

csv_colums = ['Coin name', 'Market', 'Currency', 'Price', 'Open 24H', 'Range 24H']



with open('datacoins.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(csv_colums)
    csvwriter.writerow(list)
