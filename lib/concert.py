# lib/concert.py
class Concert:
    _all = []
    
    def __init__(self, date, band, venue):
        self._date = None
        self._band = None
        self._venue = None
        self.date = date
        self.band = band
        self.venue = venue
        Concert._all.append(self)
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        # If not valid, don't change it
    
    @property
    def band(self):
        return self._band
    
    @band.setter
    def band(self, value):
        # Check if it's a Band instance
        if hasattr(value, '_concerts'):  # Check for Band attribute
            # Remove from old band's concerts if changing
            if self._band and self in self._band._concerts:
                self._band._concerts.remove(self)
            
            self._band = value
            if self not in value._concerts:
                value._concerts.append(self)
        # If not valid, don't change it
    
    @property
    def venue(self):
        return self._venue
    
    @venue.setter
    def venue(self, value):
        # Check if it's a Venue instance
        if hasattr(value, '_concerts'):  # Check for Venue attribute
            # Remove from old venue's concerts if changing
            if self._venue and self in self._venue._concerts:
                self._venue._concerts.remove(self)
            
            self._venue = value
            if self not in value._concerts:
                value._concerts.append(self)
        # If not valid, don't change it
    
    def hometown_show(self):
        return self.band.hometown == self.venue.city
    
    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"