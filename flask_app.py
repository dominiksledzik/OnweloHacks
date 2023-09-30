from flask import Flask, request
from crypto_api_endpoints.cogingeco import CoginGeco
app = Flask(__name__)


@app.route('/crypto/')
def get_json():
    shortcuts = request.args.getlist('shortcuts')
    return CoginGeco.get_prices(*shortcuts)

    