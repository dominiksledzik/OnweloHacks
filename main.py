from crypto_api_endpoints.cogingeco import CoginGeco
from crypto_api_endpoints.kucoin import Kucoin
from crypto_api_endpoints.bitfinex import Bitfinex
from crypto_api_endpoints.zonda import Zonda
from req import get_usd_from_NBP
import json

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


user_input = ["Zonda", "Bitfinex", "CoginGeco", "Kucoin"]
markets = factory(user_input)

currencies = {"BTC": 1.3, "ETH": 15, "DOGE": 7899, "XRP": 3}

output = []
for idx, market in enumerate(markets):
    market_prices = market.get_prices(*currencies.keys())
    market_prices["market"] = user_input[idx]
    output.append(market_prices)

usd_to_pln = get_usd_from_NBP()
with open("cryptocurrency.json", "r") as f:
    crypto_names = json.load(f)



final_output = {"nbp_usd_pln": usd_to_pln, "cryptocurrencies": []}
for currency in currencies:
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
            pass
        exchanges.append(market_data)

    final_output["cryptocurrencies"].append(
        {
            "code": currency.lower(),
            "name": crypto_names[currency],
            "volume": currencies[currency],
            "exchanges": exchanges
        } 
    )