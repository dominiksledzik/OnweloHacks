from .crypto_api_endpoints.cogingeco import CoginGeco
from .crypto_api_endpoints.kucoin import Kucoin
from .crypto_api_endpoints.bitfinex import Bitfinex
from .crypto_api_endpoints.zonda import Zonda
import json
import requests


def factory(user_input: list[str]):
 
    """Factory Method"""
    markets = {
        "CoginGeco": CoginGeco,
        "Kucoin": Kucoin,
        "Bitfinex": Bitfinex,
        "Zonda": Zonda
    }
    output = []
    for input in user_input:
        output.append(markets[input])
 
    return output


def get_data(currencies: dict[str, float]):
    market_names = ["Zonda", "Bitfinex", "CoginGeco", "Kucoin"]
    markets = factory(market_names)

    output = []
    for idx, market in enumerate(markets):
        market_prices = market.get_prices(*currencies.keys())
        market_prices["market"] = market_names[idx]
        output.append(market_prices)

    usd_to_pln = get_usd_from_NBP()
    with open("cryptocurrency.json", "r") as f:
        crypto_names = json.load(f)


    final_output = {"nbp_usd_pln": usd_to_pln, "cryptocurrencies": []}
    for currency in currencies:
        if currency not in crypto_names:
            full_name = input(f"Full name of {currency} not found. Please enter it: ")
        else:
            full_name = crypto_names[currency]
        exchanges = []
        for data in output:
            market_data = {}
            market_data["name"] = data["market"]
            try:
                if data["currency"] == "PLN":
                    market_data["pln"] = data["prices"][currency]
                else:
                    market_data["usd"] = data["prices"][currency]
                    market_data["pln"] = data["prices"][currency]*usd_to_pln
            except KeyError:
                market_data["pln"] = input(f"{currency} not found in {data['market']}. Please enter your input: ")
            exchanges.append(market_data)

        final_output["cryptocurrencies"].append(
            {
                "code": currency.lower(),
                "name": full_name,
                "volume": currencies[currency],
                "exchanges": exchanges
            }
        )
    return final_output


def get_usd_from_NBP():
    table_dict = {"table": 'A'}
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/{table}/".format(**table_dict))
    nbp_currency_lst = json.loads(response.text)[0]['rates']

    usd = [elem['mid'] for elem in nbp_currency_lst if elem['code'] == 'USD'][0]
    return usd
