from crypto_api_endpoints.cogingeco import CoginGeco
from crypto_api_endpoints.kucoin import Kucoin


def factory(user_input: list[str]):
 
    """Factory Method"""
    markets = {
        "CoginGeco": CoginGeco,
        "Kucoin": Kucoin,
    }
    output = []
    for input in user_input:
        output.append(markets[input])
 
    return output

user_input = ["CoginGeco", "Kucoin"]
markets = factory(user_input)

currencies = ["BTC", "ETH"]

output = []
for market in markets:
    output.append(market.get_prices(*currencies))
    