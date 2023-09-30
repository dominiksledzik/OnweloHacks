import requests
import json


class Zonda:


    @staticmethod
    def get_price(*shortcuts):
        headers = {"content-type": "application/json"}
        json_data = None
        with open('../cryptocurrency.json','r',encoding='utf-8') as json_file:
            json_data = json.load(json_file)
        final_dict = {}
        for idx,shortcut in enumerate(shortcuts):
            url = f"https://api.zondacrypto.exchange/rest/trading/ticker/{shortcuts[idx]}-PLN"
            response = requests.request("GET", url, headers=headers, timeout=5)
            response = response.json()
            conversion_rate = float(response["ticker"]["rate"])
            conerted_values = {json_data[shortcut]['full_name']:{'pln':conversion_rate}}
            final_dict.update(conerted_values)
        return final_dict

    @staticmethod
    def convert():
        pass
