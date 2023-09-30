import requests
import json

cryptocurrencyValue = 'BTC'
currency = 'PLN'

url = f"https://api.zondacrypto.exchange/rest/trading/ticker/{cryptocurrencyValue}-{currency}"

headers = {'content-type': 'application/json'}

response = requests.request("GET", url, headers=headers)

# print(response.text)
x = json.loads(response.text)
conversion = {
    "conversion_rate": x['ticker']['rate'],
    "crypto" : cryptocurrencyValue,
    "currency": currency
}

print(conversion)
