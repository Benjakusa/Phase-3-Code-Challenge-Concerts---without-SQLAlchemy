# lib/band.py
class Band:
    _all = []
    
    def __init__(self, name, hometown):
        self.name = name
        self._hometown = hometown
        self._concerts = []
        Band._all.append(self)
    
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
    def hometown(self):
        return self._hometown
    
    @property
    def concerts(self):
        return self._concerts if self._concerts else None
    
    @property
    def venues(self):
        if not self._concerts:
            return None
        venues_list = []
        for concert in self._concerts:
            if concert.venue not in venues_list:
                venues_list.append(concert.venue)
        return venues_list
    
    def play_in_venue(self, venue, date):
        from lib.concert import Concert
        concert = Concert(date, self, venue)
        return concert
    
    def all_introductions(self):
        if not self._concerts:
            return None
        introductions = []
        for concert in self._concerts:
            introductions.append(concert.introduction())
        return introductions