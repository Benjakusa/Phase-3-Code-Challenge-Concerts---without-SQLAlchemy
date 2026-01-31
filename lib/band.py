# lib/band.py
class Band:
    _all = []
    
    def __init__(self, name, hometown):
        self._name = None  # Initialize first
        self._hometown = hometown
        self._concerts = []
        self.name = name  # Use setter for validation
        Band._all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        # If not valid, don't change it (for regular tests)
        # For bonus: uncomment the raise Exception lines
    
    @property
    def hometown(self):
        return self._hometown
    
    @property
    def concerts(self):
        return self._concerts or None
    
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