from flask import Flask, request, render_template
from crypto_api_endpoints.cogingeco import CoginGeco
import json

app = Flask(__name__,template_folder='./frontend/template')

@app.route('/test/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input', '').split('\n')

    else:
        user_input = []
   
    return render_template('index.html',user_input=user_input)

@app.route('/crypto/', methods=['GET'])
def get_json():
    shortcuts = request.args.getlist('shortcuts')
    return CoginGeco.get_prices(*shortcuts)


@app.route('/crypto_shortcuts/', methods=['GET'])
def get_crypto():
    with open('cryptocurrency.json', 'r') as json_file:
        return json.load(json_file)
    
@app.route('/gettemplate', methods=["GET","POST"])
def dropdown():
    cryptocurrencies = ['BTC','ETH']
    return render_template('index.html', cryptocurrencies = cryptocurrencies)
