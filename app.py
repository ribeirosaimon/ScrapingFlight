import json

import flask
from flask import Flask
from flask_cors import CORS

from Services.Calculator import CalculatorTravel
from Model.Repository import ConectDb

app = Flask(__name__)
cors = CORS(app, resources={"/*": {"origins": "*"}})

@app.route("/")
def getFlightScraping():
    result = CalculatorTravel().best_price()
    ConectDb().addDocument(**result)
    return result
