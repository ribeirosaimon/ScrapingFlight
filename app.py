from Services.Calculator import CalculatorTravel
from Model.FlightDTO import FlightDTO
import datetime
import time


if __name__ == '__main__':
    print('Welcome to my Script')
    while True:
        result = CalculatorTravel().best_price()
        FlightDTO().saveFlight(**result)
        print('------------------------------------')
        print(datetime.datetime.now())
        print(result)
        print('------------------------------------')
        print('------------------------------------')
        time.sleep(60)
