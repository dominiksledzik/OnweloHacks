import requests
import json 

def get_usd_from_NBP():
    table_dict = {"table": 'A'}
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/{table}/".format(**table_dict))
    nbp_currency_lst = json.loads(response.text)[0]['rates']

    usd = [elem['mid'] for elem in nbp_currency_lst if elem['code'] == 'USD'][0]
    return usd
