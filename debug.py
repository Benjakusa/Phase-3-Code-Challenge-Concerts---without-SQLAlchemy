# debug.py
#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib.band import Band
from lib.venue import Venue
from lib.concert import Concert

def test_name_mutability():
    """Test that names can be changed but invalid values don't change them"""
    print("Testing name mutability...")
    
    band = Band("boygenius", "NYC")
    print(f"Initial name: {band.name}")
    
    # Valid change
    band.name = "spicegurls"
    print(f"After valid change: {band.name}")
    
    # Invalid change (should not change the name)
    band.name = 7
    print(f"After invalid change (should still be 'spicegurls'): {band.name}")
    
    # Another invalid change
    band.name = ""
    print(f"After empty string (should still be 'spicegurls'): {band.name}")

def test_concert_relationships():
    """Test concert relationships work correctly"""
    print("\nTesting concert relationships...")
    
    band1 = Band("The Beatles", "Liverpool")
    band2 = Band("The Rolling Stones", "London")
    venue1 = Venue("Cavern Club", "Liverpool")
    venue2 = Venue("Shea Stadium", "New York")
    
    # Create concerts
    concert1 = Concert("1962-08-01", band1, venue1)
    concert2 = Concert("1965-08-15", band1, venue2)
    
    print(f"Band1 concerts: {len(band1.concerts) if band1.concerts else 0}")
    print(f"Venue1 concerts: {len(venue1.concerts) if venue1.concerts else 0}")
    
    # Test changing band on a concert
    print("\nChanging concert band...")
    concert1.band = band2
    print(f"Concert1 band is now: {concert1.band.name}")
    print(f"Band1 now has {len(band1.concerts) if band1.concerts else 0} concerts")
    print(f"Band2 now has {len(band2.concerts) if band2.concerts else 0} concerts")
    
    # Test changing venue
    print("\nChanging concert venue...")
    concert1.venue = venue2
    print(f"Concert1 venue is now: {concert1.venue.name}")
    print(f"Venue1 now has {len(venue1.concerts) if venue1.concerts else 0} concerts")
    print(f"Venue2 now has {len(venue2.concerts) if venue2.concerts else 0} concerts")

if __name__ == "__main__":
    print("=" * 50)
    print("Testing Concert Domain System")
    print("=" * 50)
    
    test_name_mutability()
    test_concert_relationships()
    
    print("\n" + "=" * 50)
    print("Tests completed!")
    print("=" * 50)