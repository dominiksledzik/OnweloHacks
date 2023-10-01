import requests


class Zonda:


    @staticmethod
    def get_prices(*shortcuts):
        headers = {"content-type": "application/json"}
        
        output = {}
        for shortcut in shortcuts:
            url = f"https://api.zondacrypto.exchange/rest/trading/ticker/{shortcut}-PLN"
            response = requests.request("GET", url, headers=headers)
            response = response.json()
            try:
                conversion_rate = float(response["ticker"]["rate"])
            except KeyError:
                continue
            output[shortcut] = conversion_rate
        
        final_output = {"currency": "PLN", "prices": output}
        return final_output

    @staticmethod
    def convert():
        pass
