import scrapy


class CreateUrls:
    def __init__(self):
        self.base_url = "https://www.decolar.com/passagens-aereas"
        self.america = ['fln', 'sao', 'cpq']
        self.europe = ['ber', 'mad', 'lon', 'par', 'fra', 'muc']
        self.args_api = '?searchType=ONEWAY&reSearch=true'

    def departure_url(self):
        all_urls = []
        for br_departure in self.america:
            for europe_arrival in self.europe:
                all_urls.append(
                    f'{self.base_url}/{br_departure}/{europe_arrival}/{self.args_api}')
        return all_urls

    def arrival_url(self):
        all_urls = []
        for europe_arrival in self.europe:
            for br_departure in self.america:
                all_urls.append(
                    f'{self.base_url}/{europe_arrival}/{br_departure}/{self.args_api}')
        return all_urls

    def departure_arrival_url(self):
        return self.departure_url() + self.arrival_url()


class FlightSpider(scrapy.Spider):
    name = 'flight'

    # start_urls = CreateUrls().departure_arrival_url()
    start_urls = [
        "https://www.decolar.com/passagens-aereas/FLN/MAD?from=SB&di=1-0&searchType=ONEWAY&reSearch=true"]

    def parse(self, response):
        table = response.xpath(
            '//ul[@class="matrix-airline-4"]')
        print('----------------------------------')
        print(response.xpath('//*[@id="toolbox-tabs-position"]/toolbox-tabs/div/tabs/div/div[2]/tab[1]/div/airlines-matrix/span[1]/div/div/div/div/airlines-matrix-airline[1]/ul/li[3]/span/flights-price/span/flights-price-element/span/span/em/span[2]'))
        print(dir(response.body))
        print('----------------------------------')
        price = table.xpath('//span[@class="amount price-amount"]/text()')

        yield {
            'price': price,
            'title': 'title',
            'link': 'link'
        }
