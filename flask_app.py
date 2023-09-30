from flask import Flask, request, render_template
from crypto_api_endpoints.cogingeco import CoginGeco
app = Flask(__name__,template_folder='./frontend/template')


@app.route('/crypto/')
def get_json():
    shortcuts = request.args.getlist('shortcuts')
    return CoginGeco.get_prices(*shortcuts)
