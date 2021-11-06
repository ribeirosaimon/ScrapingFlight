import requests
from bs4 import BeautifulSoup


class ScrapingFlight:

    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)

    def get_flight_informations(self):
        list_return = []
        soup = BeautifulSoup(self.response.content, 'html.parser')
        script = soup.find_all('script')[8].text.split('"jsonData"')
        jsonData = script[1].split('"fareSelectorType"')
        print(jsonData[0][2:-1])
        print(len(jsonData))
        # json_data = script.text.split('\nvar')[2]
        # routes = json_data.split('routes')[1]
        # textDetails = routes.split('fromTextDetail')[0]

        # self.string_treatment(textDetails)
        # complet = routes.split('fromTextDetail')[1]
        # all_travel = textDetails.split('departure')

        # for x in all_travel:
        #     if "airportCode" in x:
        #         dict_travel = {}
        #         flight = x.replace("'", "").replace('"', "")[
        #             1:-2].replace('{', '').replace('}', '').split(',')
        #         dict_travel['airport'] = flight[0].split(':')[1]
        #         dict_travel['dateDeparture'] = flight[1].split('date:')[1]
        #         dict_travel['arrival'] = flight[3].split(':')[-1]
        #         dict_travel['dateArrival'] = flight[1].split('date:')[1]
        #         dict_travel['airLine'] = flight[6].split(':')[-1]
        #         dict_travel['flightId'] = flight[7].split(':')[-1]
        #         dict_travel['duration'] = flight[-1].split('duration:')[-1]
        #         list_return.append(dict_travel)
        # return {'travel': list_return}

    def string_treatment(self, fligh_string):
        print(fligh_string)
