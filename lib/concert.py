# lib/concert.py
class Concert:
    _all = []
    
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert._all.append(self)
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string")
        if len(value) <= 0:
            raise Exception("Date must be greater than zero characters")
        self._date = value
    
    @property
    def band(self):
        return self._band
    
    @band.setter
    def band(self, value):
        if not hasattr(value, 'name'):  # Simple check if it's a Band instance
            raise Exception("Band must be of type Band")
        self._band = value
        # Add this concert to the band's concerts
        value._concerts.append(self)
    
    @property
    def venue(self):
        return self._venue
    
    @venue.setter
    def venue(self, value):
        if not hasattr(value, 'name'):  # Simple check if it's a Venue instance
            raise Exception("Venue must be of type Venue")
        self._venue = value
        # Add this concert to the venue's concerts
        value._concerts.append(self)
    
    def hometown_show(self):
        return self.band.hometown == self.venue.city
    
    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"