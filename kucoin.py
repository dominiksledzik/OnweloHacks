import requests

class Kucoin():
    def __init__(self) -> None:
        self.url = "https://api.kucoin.com/api/v1/prices"

    def get_prices(self, currencies: list[str]):
        json_output = self.send_requests(currencies)
        prices = self.extract_prices(json_output)

        return prices

    def send_requests(self, currencies: list[str]):
        response = requests.request('GET', host + url, params={"base": "PLN", "currencies": currencies})
        json_output = response.json()

        return json_output

    def extract_prices(self, json_output: dict[str]):
        data = json_output["data"]
        output = {"conversion_currency": "PLN", "prices": data}

        return output







host = "https://api.kucoin.com"
#headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

url = '/api/v1/prices'
query_param = ''
r = requests.request('GET', host + url, params={"base": "PLN", "currencies": ["ETH", "BTC"]})
print(r.json())