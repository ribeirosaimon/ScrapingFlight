from Services.Treatment import StringTreatment
from bs4 import BeautifulSoup
import requests
import json


class ScrapingFlight:

    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)

    def _scraping(self):
        soup = BeautifulSoup(self.response.content, 'html.parser')
        script = soup.find_all('script')[8].text.split('"jsonData"')
        return json.loads(script[1].split('"fareSelectorType"')[
                              0][2:-2])

    def get_json_travel_info(self, oneway=False):
        try:
            info = {}
            jsonInfos = self._scraping()
            jsonData = jsonInfos['seoFaqParameters']
            info['origin'] = jsonInfos['origin']['code']
            info['destination'] = jsonInfos['destination']['code']
            info['travelAt'] = StringTreatment().month_treatment(
                jsonData['cheapestMonth'])
            if oneway:
                info['travel'] = 'oneway'
                info['time'] = StringTreatment().time_treatment(
                    jsonData['fastestGoing'])
            else:
                info['travel'] = 'roundtrip'
                info['timeGoing'] = StringTreatment().time_treatment(
                    jsonData['fastestGoing'])
                info['timeReturn'] = StringTreatment().time_treatment(
                    jsonData['fastestReturn'])
            info['price'] = int(jsonData['cheapestPrice'].replace(
                'R$', '').replace('.', '').replace(',', '.').strip(' '))
            info['airlines'] = jsonData['airlinesNames'].split(',')
            return info
        except:
            info['price'] = 0
            return info
