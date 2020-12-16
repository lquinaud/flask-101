# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def products():
    PRODUCTS = {
      1: { 'id': 1, 'name': 'Skello' },
      2: { 'id': 2, 'name': 'Socialive.tv' },
    }
    #return jsonify(name=("Skello","Socialive.tv"), id=(1,2))
    return jsonify(PRODUCTS)

