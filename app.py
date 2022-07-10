from Services.Calculator import CalculatorTravel
from Model.Repository import ConectDb
import datetime
import time


if __name__ == '__main__':
    print('Welcome to my Script')
    while True:
        result = CalculatorTravel().best_price()
        ConectDb().addDocument(**result)
        print("I make scraping and i return this: ")
        print(result)
        print('------------------------------------')
        time.sleep(60*5)
