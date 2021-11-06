from Services.Scraping import ScrapingFlight

url = 'https://www.decolar.com/passagens-aereas/SAO/PAR?from=SB&di=1-0&searchType=ONEWAY&reSearch=true'
ScrapingFlight(url).get_flight_informations()
