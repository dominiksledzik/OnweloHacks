from flask import Flask, request, render_template
from crypto_api_endpoints.cogingeco import CoginGeco
import json

app = Flask(__name__,template_folder='./frontend/template')

@app.route('/crypto/', methods=['GET'])
def get_json():
    shortcuts = request.args.getlist('shortcuts')
    return CoginGeco.get_prices(*shortcuts)


@app.route('/crypro_shortcuts/', methods=['GET'])
def get_crypto():
    with open('cryptocurrency.json', 'r') as json_file:
        return json.load(json_file)
    
@app.route('/gettemplate', methods=["GET","POST"])
def dropdown():
    cryptocurrencies = ['BTC','ETH']
    return render_template('index.html', cryptocurrencies = cryptocurrencies)
