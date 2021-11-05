import requests
from bs4 import BeautifulSoup

url = 'https://www.decolar.com/passagens-aereas/SAO/LON?from=SB&di=1-0&searchType=ONEWAY&reSearch=true'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
script = soup.find_all('script')[8]
json_data = script.text.split('\nvar')[2]
routes = json_data.split('routes')[1]
departure = routes.split('fromTextDetail')[0]
complet = routes.split('fromTextDetail')[1]


a = departure.split('departure')

list_departure = []

for x in a:
    if "airportCode" in x:
        print('ok')
        aviao = x.replace("'", "").replace('"', "")[1:-2]
        list_departure.append(aviao)
print(list_departure[0])
