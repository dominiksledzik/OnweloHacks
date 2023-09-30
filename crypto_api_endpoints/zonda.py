import requests

url = "https://api.zondacrypto.exchange/rest/trading/ticker/BTC-PLN"

headers = {'content-type': 'application/json'}

response = requests.request("GET", url, headers=headers)

print(response.text)