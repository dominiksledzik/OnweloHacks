import requests

class Kucoin():

    @staticmethod
    def get_prices(*shortcuts):
        url = "https://api.kucoin.com/api/v1/prices"
        response = requests.request('GET', url, params={"base": "PLN", "currencies": shortcuts})
        json_output = response.json()

        return json_output

    @staticmethod
    def extract_prices(self, json_output: dict[str]):
        pass
        # data = json_output["data"]
        # output = {"conversion_currency": "PLN", "prices": data}

        # return output