from crypto_api_endpoints.coingeco import CoginGeco
from kucoin import Kucoin


def factory(user_input: list[str]):
 
    """Factory Method"""
    markets = {
        "CoinGeco": CoginGeco,
        "Kucoin": Kucoin,
    }
    output = []
    for input in user_input:
        output.append(markets[input])
 
    return output

user_input = ["CoinGeco", "Kucoin"]
markets = factory(user_input)

currencies = ["BTC", "ETH"]

output = []
for market in markets:
    output.append(market.get_prices(currencies))

