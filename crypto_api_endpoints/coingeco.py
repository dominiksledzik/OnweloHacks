import requests
import json


class CoginGeco:


    @staticmethod
    def get_prices(*shortcuts):

        with open("./cryptocurrency.json", 'r') as json_file:
            available_cryptocurrency = json.load(json_file)
        
        ids = [available_cryptocurrency[shortcut]['full_name'].lower() 
               for shortcut in shortcuts]

        url = f"https://api.coingecko.com/api/v3/simple/price?ids="
        for id in ids:
             url += f"{id},"
        url = f"{url[:-1]}&vs_currencies=pln"

        headers = {'content-type': 'application/json'}
        response = requests.request("GET", url, headers=headers)

        return json.loads(response.text)

    @staticmethod
    def conversion():
        pass

CoginGeco.get_prices("BTC", "ETH")
