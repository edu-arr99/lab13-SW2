from flask import Flask
from flask import request, jsonify
import urllib.request, json
from werkzeug.exceptions import HTTPException
import requests

app = Flask(__name__)

# Do not remove this method.
@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

@app.route('/igv')
def igv():
    tax = get_tax_from_api()

    return jsonify(igv=tax), 200

def get_tax_from_api():
    url = "http://127.0.0.1:5001/tax"

    response = requests.get(url, data="GG")
    data = response.json()

    return data["Tax"]

if __name__ == "__main__":
    app.run(debug=True, port=8080)