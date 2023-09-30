import requests


class Bitfinex():

    @staticmethod
    def get_prices(*shortcuts):
        url = "https://api.bitfinex.com/v1/pubticker/"

        output = {}
        for shortcut in shortcuts:
            pair = ""
            if len(shortcut) > 3:
                pair = f"{shortcut}:USD"
            else:
                pair = f"{shortcut}USD"

            response = requests.get(url + pair)
            data = response.json()
            output[shortcut] = float(data["last_price"])

        final_output = {"currency": "USD", "prices": output}
        return final_output
    
    @staticmethod
    def conversion():
        pass
