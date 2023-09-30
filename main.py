from crypto_api_endpoints.cogingeco import CoginGeco
from crypto_api_endpoints.kucoin import Kucoin
from crypto_api_endpoints.bitfinex import Bitfinex
from crypto_api_endpoints.zonda import Zonda

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


user_input = ["CoginGeco", "Kucoin", "Bitfinex", "Zonda"]
markets = factory(user_input)

currencies = ["BTC", "ETH"]

output = []
for idx, market in enumerate(markets):
    market_prices = market.get_prices(*currencies)
    market_prices["market"] = user_input[idx]
    output.append(market_prices)

print(output)