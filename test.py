import json


x = None
with open('../cryptocurrency.json','r') as f:
    x = json.load(f)
print(x['BTC']['full_name'])