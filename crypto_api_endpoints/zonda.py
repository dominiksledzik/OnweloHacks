import requests
import json

cryptocurrencyName = 'BTC' #TODO: delete //placeholder
currencyName = 'PLN' #TODO: delete //placeholder

cryptoValue = 4.66 #TODO delete that // change vlaue to what i taken from the formula.

url = f"https://api.zondacrypto.exchange/rest/trading/ticker/{cryptocurrencyName}-{currencyName}"

headers = {'content-type': 'application/json'}

response = requests.request("GET", url, headers=headers)


response_json = json.loads(response.text)
conversionRate = float(response_json['ticker']['rate'])

conversion = {
    "conversion_rate": conversionRate,
    "crypto" : cryptocurrencyName,
    "currency": currencyName
}

finalValueZloty = format(cryptoValue * conversionRate, '.2f')
