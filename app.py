import json
from Services.Calculator import CalculatorTravel
from Model.Repository import ConectDb
import datetime
import time

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    result = CalculatorTravel().best_price()
    ConectDb().addDocument(**result)
    return json.decoder(result)
