import requests
import json


class CoginGeco:


    @staticmethod
    def get_prices(*shortcuts):

        with open("./cryptocurrency.json", 'r') as json_file:
            available_cryptocurrency = json.load(json_file)
        
        ids = [available_cryptocurrency[shortcut]['full_name'].lower() 
               for shortcut in shortcuts]

        url = CoginGeco.get_uri(ids)
        headers = {'content-type': 'application/json'}

        response = requests.request("GET", url, headers=headers)
        result = response.json()

        usa_shortcuts = set(ids) - set(result.keys())

        if len(usa_shortcuts) > 0:
            url = CoginGeco.get_uri(ids)
            usa_response = requests.request("GET", url, headers=headers)
            result = result.update(usa_response)

        return result

    @staticmethod
    def get_uri(ids):
        url = f"https://api.coingecko.com/api/v3/simple/price?ids="
        for id in ids:
             url += f"{id},"
        return f"{url[:-1]}&vs_currencies=pln"
        
    
    @staticmethod
    def conversion():
        pass

CoginGeco.get_prices("BTC", "ETH")
