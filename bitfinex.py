import requests


# connect to bitfinex API
def get_bitfinex_data(url):
    response = requests.get(url)
    data = response.json()
    return data


url = "https://api.bitfinex.com/v1/pubticker/btcusd"

print(get_bitfinex_data(url))

'''
Output:

 {
    "mid": "26955.5",
    "bid": "26955.0",
    "ask": "26956.0",
    "last_price": "26955.0",
    "low": "26708.0",
    "high": "27111.0",
    "volume": "743.42641419",
    "timestamp": "1696079194.9840236",
}

'''

# get bitfinex data for DOGE
url1 = "https://api.bitfinex.com/v1/pubticker/doge:usd"
print(get_bitfinex_data(url1))



''' coin_pairs = [
    [
        "1INCH:USD",
        "1INCH:UST",
        "AAVE:USD",
        "AAVE:UST",
        "ADABTC",
        "ADAUSD",
        "ADAUST",
        "ALGBTC",
        "ALGUSD",
        "ALGUST",
        "AMPBTC",
        "AMPUSD",
        "AMPUST",
        "ANTBTC",
        "ANTUSD",
        "APENFT:USD",
        "APENFT:UST",
        "APEUSD",
        "APEUST",
        "APTUSD",
        "APTUST",
        "ARBUSD",
        "ARBUST",
        "ATLAS:USD",
        "ATLAS:UST",
        "ATOBTC",
        "ATOUSD",
        "ATOUST",
        "AVAX:BTC",
        "AVAX:USD",
        "AVAX:UST",
        "AXSUSD",
        "AXSUST",
        "B2MUSD",
        "B2MUST",
        "BALUSD",
        "BALUST",
        "BAND:USD",
        "BAND:UST",
        "BATUSD",
        "BCHABC:USD",
        "BCHN:USD",
        "BEST:USD",
        "BGBUSD",
        "BGBUST",
        "BLUR:USD",
        "BLUR:UST",
        "BMNBTC",
        "BMNUSD",
        "BNTUSD",
        "BOBA:USD",
        "BOSON:USD",
        "BOSON:UST",
        "BRISE:USD",
        "BRISE:UST",
        "BTC:CNHT",
        "BTC:MXNT",
        "BTC:XAUT",
        "BTCEUR",
        "BTCEUT",
        "BTCGBP",
        "BTCJPY",
        "BTCMIM",
        "BTCTRY",
        "BTCUSD",
        "BTCUST",
        "BTSE:USD",
        "BTTUSD",
        "CCDBTC",
        "CCDUSD",
        "CCDUST",
        "CHEX:USD",
        "CHSB:BTC",
        "CHSB:USD",
        "CHSB:UST",
        "CHZUSD",
        "CHZUST",
        "CLOUSD",
        "CNH:CNHT",
        "COMP:USD",
        "COMP:UST",
        "CRVUSD",
        "CRVUST",
        "DAIBTC",
        "DAIUSD",
        "DGBUSD",
        "DOGE:BTC",
        "DOGE:USD",
        "DOGE:UST",
        "DORA:USD",
        "DOTBTC",
        "DOTUSD",
        "DOTUST",
        "DSHBTC",
        "DSHUSD",
        "DUSK:BTC",
        "DUSK:USD",
        "DVFUSD",
        "EGLD:USD",
        "EGLD:UST",
        "EOSBTC",
        "EOSETH",
        "EOSUSD",
        "EOSUST",
        "ETCBTC",
        "ETCUSD",
        "ETCUST",
        "ETH2X:ETH",
        "ETH2X:USD",
        "ETH2X:UST",
        "ETH:MXNT",
        "ETH:XAUT",
        "ETHBTC",
        "ETHEUR",
        "ETHEUT",
        "ETHGBP",
        "ETHJPY",
        "ETHUSD",
        "ETHUST",
        "ETHW:USD",
        "ETHW:UST",
        "EURUST",
        "EUT:MXNT",
        "EUTEUR",
        "EUTUSD",
        "EUTUST",
        "FBTUSD",
        "FBTUST",
        "FCLUSD",
        "FCLUST",
        "FETUSD",
        "FETUST",
        "FILUSD",
        "FILUST",
        "FLOKI:USD",
        "FLOKI:UST",
        "FLRUSD",
        "FLRUST",
        "FORTH:USD",
        "FORTH:UST",
        "FTMUSD",
        "FTMUST",
        "FUNUSD",
        "GALA:USD",
        "GALA:UST",
        "GBPEUT",
        "GBPUST",
        "GNOUSD",
        "GOCUSD",
        "GOCUST",
        "GRTUSD",
        "GRTUST",
        "GTXUSD",
        "GTXUST",
        "HIXUSD",
        "HIXUST",
        "HMTUSD",
        "HMTUST",
        "HTXUSD",
        "HTXUST",
        "ICEUSD",
        "ICPUSD",
        "ICPUST",
        "IDXUSD",
        "IOTBTC",
        "IOTUSD",
        "JASMY:USD",
        "JASMY:UST",
        "JPYUST",
        "JSTBTC",
        "JSTUSD",
        "JSTUST",
        "KANUSD",
        "KANUST",
        "KARATE:USD",
        "KARATE:UST",
        "KAVA:USD",
        "KAVA:UST",
        "KNCUSD",
        "KSMUSD",
        "KSMUST",
        "LAIUSD",
        "LAIUST",
        "LDOUSD",
        "LDOUST",
        "LEOBTC",
        "LEOETH",
        "LEOUSD",
        "LEOUST",
        "LINK:USD",
        "LINK:UST",
        "LRCUSD",
        "LTCBTC",
        "LTCUSD",
        "LTCUST",
        "LUNA2:USD",
        "LUNA2:UST",
        "LUXO:USD",
        "LYMUSD",
        "MATIC:BTC",
        "MATIC:USD",
        "MATIC:UST",
        "MIMUSD",
        "MIMUST",
        "MKRUSD",
        "MKRUST",
        "MLNUSD",
        "MNABTC",
        "MNAUSD",
        "MOBUSD",
        "MOBUST",
        "MXNT:USD",
        "NEAR:USD",
        "NEAR:UST",
        "NEOBTC",
        "NEOUSD",
        "NEOUST",
        "NEXO:BTC",
        "NEXO:USD",
        "NEXO:UST",
        "NOMUSD",
        "NOMUST",
        "NXRA:USD",
        "OCEAN:USD",
        "OCEAN:UST",
        "OGNUSD",
        "OGNUST",
        "OMGBTC",
        "OMGETH",
        "OMGUSD",
        "OMNUSD",
        "ONEUSD",
        "ONEUST",
        "OPXUSD",
        "OPXUST",
        "PAXUSD",
        "PAXUST",
        "PEPE:USD",
        "PEPE:UST",
        "PLANETS:USD",
        "PLANETS:UST",
        "PLUUSD",
        "PNKUSD",
        "POLC:USD",
        "POLIS:USD",
        "POLIS:UST",
        "QRDO:USD",
        "QRDO:UST",
        "QTFBTC",
        "QTFUSD",
        "QTMUSD",
        "RBTUSD",
        "REQUSD",
        "RLYUSD",
        "RLYUST",
        "RRTUSD",
        "SAND:USD",
        "SAND:UST",
        "SEIUSD",
        "SEIUST",
        "SENATE:USD",
        "SGBUSD",
        "SGBUST",
        "SHFT:USD",
        "SHFT:UST",
        "SHIB:USD",
        "SHIB:UST",
        "SIDUS:USD",
        "SMRUSD",
        "SMRUST",
        "SNXUSD",
        "SNXUST",
        "SOLBTC",
        "SOLUSD",
        "SOLUST",
        "SPELL:USD",
        "STGUSD",
        "STGUST",
        "SUIUSD",
        "SUIUST",
        "SUKU:USD",
        "SUKU:UST",
        "SUNUSD",
        "SUNUST",
        "SUSHI:USD",
        "SUSHI:UST",
        "SWEAT:USD",
        "SWEAT:UST",
        "SXXUSD",
        "TENET:USD",
        "TENET:UST",
        "TESTADA:TESTUSD",
        "TESTALGO:TESTUSD",
        "TESTAPT:TESTUSD",
        "TESTAVAX:TESTUSD",
        "TESTBTC:TESTUSD",
        "TESTBTC:TESTUSDT",
        "TESTDOGE:TESTUSD",
        "TESTDOT:TESTUSD",
        "TESTEOS:TESTUSD",
        "TESTETH:TESTUSD",
        "TESTFIL:TESTUSD",
        "TESTLTC:TESTUSD",
        "TESTMATIC:TESTUSD",
        "TESTMATIC:TESTUSDT",
        "TESTNEAR:TESTUSD",
        "TESTSOL:TESTUSD",
        "TESTXAUT:TESTUSD",
        "TESTXTZ:TESTUSD",
        "THETA:USD",
        "THETA:UST",
        "TLOS:USD",
        "TOMI:USD",
        "TOMI:UST",
        "TONUSD",
        "TONUST",
        "TRADE:USD",
        "TRADE:UST",
        "TREEB:USD",
        "TRXBTC",
        "TRXETH",
        "TRXEUR",
        "TRXUSD",
        "TRXUST",
        "TRYUST",
        "TSDUSD",
        "TSDUST",
        "UDCUSD",
        "UDCUST",
        "UNIUSD",
        "UNIUST",
        "UOSBTC",
        "UOSUSD",
        "UST:CNHT",
        "UST:MXNT",
        "USTUSD",
        "UTKUSD",
        "VETBTC",
        "VETUSD",
        "VETUST",
        "VRAUSD",
        "VRAUST",
        "VSYUSD",
        "WAVES:USD",
        "WAVES:UST",
        "WBTBTC",
        "WBTUSD",
        "WHBT:USD",
        "WHBT:UST",
        "WILD:USD",
        "WILD:UST",
        "WMINIMA:USD",
        "WMINIMA:UST",
        "WNCG:USD",
        "WOOUSD",
        "WOOUST",
        "XAUT:BTC",
        "XAUT:USD",
        "XAUT:UST",
        "XCAD:USD",
        "XCNUSD",
        "XDCUSD",
        "XDCUST",
        "XLMBTC",
        "XLMUSD",
        "XLMUST",
        "XMRBTC",
        "XMRUSD",
        "XMRUST",
        "XRDBTC",
        "XRDUSD",
        "XRPBTC",
        "XRPUSD",
        "XRPUST",
        "XTZBTC",
        "XTZUSD",
        "XTZUST",
        "XVGUSD",
        "YFIUSD",
        "YFIUST",
        "ZECBTC",
        "ZECUSD",
        "ZILUSD",
        "ZRXUSD",
    ]
]


'''