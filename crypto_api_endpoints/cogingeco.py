import requests
import json


class CoginGeco:


    @staticmethod
    def get_prices(*shortcuts):

        list_url = "https://api.coingecko.com/api/v3/coins/list"
        response = requests.request("GET", list_url)
        currency_ids = response.json()
        shortcut_id_pairs = {}
        for shortcut in shortcuts:
            for currency_id in currency_ids:
                if shortcut.lower() == currency_id["symbol"]:
                    shortcut_id_pairs[currency_id["id"]] = shortcut


        url = f"https://api.coingecko.com/api/v3/simple/price?ids="
        for id in shortcut_id_pairs.keys():
             url += f"{id},"
        url = f"{url[:-1]}&vs_currencies=pln"

        headers = {'content-type': 'application/json'}
        response = requests.request("GET", url, headers=headers)
        response = response.json()
        output = {}
        for id in shortcut_id_pairs:
            output[shortcut_id_pairs[id]] = response[id]["pln"]

        final_output = {"currency": "PLN", "prices": output}

        return final_output

    @staticmethod
    def conversion():
        pass

