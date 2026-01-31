# classes/many_to_many.py
class Band:
    _all = []
    
    def __init__(self, name, hometown):
        self._name = None
        self._hometown = None
        self._concerts = []
        self.name = name
        self.hometown = hometown  # Use setter
        Band._all.append(self)
    
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
        # For regular tests: only set on initialization
        # If _hometown is already set, don't change it
        if self._hometown is None and isinstance(value, str) and len(value) > 0:
            self._hometown = value
    
    def concerts(self):
        return self._concerts or None
    
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