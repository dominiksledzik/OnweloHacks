import requests
import json

class CoginGeco:

    @staticmethod
    def get_prices(*shortcuts):
        url = f"https://api.coingecko.com/api/v3/simple/price?ids="
        for shortut in shortcuts:
             url += f"{shortut},"
        url = f"{url[:-1]}&vs_currencies=usd"
        headers = {'content-type': 'application/json'}
        response = requests.request("GET", url, headers=headers)
        print(json.loads(response.text))

    @staticmethod
    def conversion():
        pass

CoginGeco.get_prices("zknftex", "bitcoin")
