# classes/many_to_many.py
class Band:
    all = []
    
    def __init__(self, name, hometown):
        self._name = None
        self._hometown = hometown
        self._concerts = []
        self.name = name
        Band.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
    
    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, value):
        # Allow assignment but don't change the value
        pass
    
    def concerts(self):
        return self._concerts if self._concerts else None
    
    def venues(self):
        if not self._concerts:
            return None
        venues_list = []
        for concert in self._concerts:
            if concert.venue not in venues_list:
                venues_list.append(concert.venue)
        return venues_list
    
    def play_in_venue(self, venue, date):
        concert = Concert(date, self, venue)
        return concert
    
    def all_introductions(self):
        if not self._concerts:
            return None
        introductions = []
        for concert in self._concerts:
            introductions.append(concert.introduction())
        return introductions


class Concert:
    all = []
    
    def __init__(self, date, band, venue):
        self._date = None
        self._band = None
        self._venue = None
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
    
    @property
    def band(self):
        return self._band
    
    @band.setter
    def band(self, value):
        if hasattr(value, '_concerts'):
            # Remove from old band's concerts if exists
            if self._band and self in self._band._concerts:
                self._band._concerts.remove(self)
            
            self._band = value
            if self not in value._concerts:
                value._concerts.append(self)
    
    @property
    def venue(self):
        return self._venue
    
    @venue.setter
    def venue(self, value):
        if hasattr(value, '_concerts'):
            # Remove from old venue's concerts if exists
            if self._venue and self in self._venue._concerts:
                self._venue._concerts.remove(self)
            
            self._venue = value
            if self not in value._concerts:
                value._concerts.append(self)
    
    def hometown_show(self):
        return self.band.hometown == self.venue.city
    
    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    all = []
    
    def __init__(self, name, city):
        self._name = None
        self._city = None
        self._concerts = []
        self.name = name
        self.city = city
        Venue.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
    
    def concerts(self):
        return self._concerts if self._concerts else None
    
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