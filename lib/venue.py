# lib/venue.py
class Venue:
    _all = []
    
    def __init__(self, name, city):
        self._name = None
        self._city = None
        self._concerts = []
        self.name = name
        self.city = city
        Venue._all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        # If not valid, don't change it
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        # If not valid, don't change it
    
    @property
    def concerts(self):
        return self._concerts or None
    
    @property
    def bands(self):
        if not self._concerts:
            return None
        bands_list = []
        for concert in self._concerts:
            if concert.band not in bands_list:
                bands_list.append(concert.band)
        return bands_list
    
    def concert_on(self, date):
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None