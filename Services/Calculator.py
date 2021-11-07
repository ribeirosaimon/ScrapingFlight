from Services.ulrs import CreateUrls
from Services.Scraping import ScrapingFlight


class CalculatorTravel:

    def __init__(self):
        self.departure = CreateUrls().departure_url()
        self.arrival = CreateUrls().arrival_url()
        self.departure_arrival = CreateUrls().complet_travel()

    def _best_price(self, list_treavel):
        all_travel, price_info = [], []
        for travel in list_treavel:
            info = ScrapingFlight(travel).get_json_travel_info(oneway=True)
            all_travel.append(info)
            if info['price'] != 0:
                price_info.append(info['price'])
        best_price = min(price_info)
        for price in all_travel:
            if best_price == price['price']:
                return price

    def best_price(self):
        best_oneway = self.oneway_travel()
        best_roundtrip = self.complet_travel()
        if best_roundtrip['price'] <= best_oneway['price']:
            return best_roundtrip
        else:
            return best_oneway

    def oneway_travel(self):
        result_dict = {}
        departure = self._best_price(self.departure)
        arrival = self._best_price(self.arrival)
        result_dict['departure'] = [
            departure['origin'], departure['destination'], departure['month'], departure['time'], departure['airlines']]
        result_dict['arrival'] = [
            arrival['origin'], arrival['destination'], arrival['month'], arrival['time'], arrival['airlines']]
        result_dict['price'] = arrival['price'] + departure['price']
        return result_dict

    def complet_travel(self):
        return self._best_price(self.departure_arrival)
