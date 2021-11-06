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
