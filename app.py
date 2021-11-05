import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.decolar.com/passagens-aereas/SAO/LON?from=SB&di=1-0&searchType=ONEWAY&reSearch=true'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
script =soup.find_all('script')[8]
json_data = script.text.split('\nvar')[2]
routes = json_data.split('routes')[1]