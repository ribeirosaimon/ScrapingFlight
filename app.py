from flask import Flask
from Services.Calculator import CalculatorTravel
from Model.Repository import ConectDb

app = Flask(__name__)

@app.route("/")
def getFlightScraping():
    result = CalculatorTravel().best_price()
    ConectDb().addDocument(**result)
    return "OK"
