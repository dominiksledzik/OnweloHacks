import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
headers = {'content-type': 'application/json'}
response = requests.request("GET", url, headers=headers)

print(response.text)
