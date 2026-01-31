# lib/venue.py
class Venue:
    _all = []
    
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self._concerts = []
        Venue._all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value) <= 0:
            raise Exception("Name must be greater than zero characters")
        self._name = value
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        if not isinstance(value, str):
            raise Exception("City must be a string")
        if len(value) <= 0:
            raise Exception("City must be greater than zero characters")
        self._city = value
    
    @property
    def concerts(self):
        return self._concerts if self._concerts else None
    
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