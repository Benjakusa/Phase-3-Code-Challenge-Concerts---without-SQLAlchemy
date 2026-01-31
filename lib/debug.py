# debug.py
#!/usr/bin/env python3

from lib.band import Band
from lib.venue import Venue
from lib.concert import Concert

def test_initialization():
    """Test basic initialization and properties"""
    print("Testing initialization...")
    
    # Create instances
    band1 = Band("The Beatles", "Liverpool")
    venue1 = Venue("Madison Square Garden", "New York")
    
    print(f"Band created: {band1.name} from {band1.hometown}")
    print(f"Venue created: {venue1.name} in {venue1.city}")
    
    # Test property validation
    try:
        band1.name = "The Rolling Stones"
        print(f"Band name changed to: {band1.name}")
    except Exception as e:
        print(f"Error changing band name: {e}")
    
    try:
        band1.name = ""  # Should raise exception
    except Exception as e:
        print(f"Expected error for empty name: {e}")
    
    try:
        band1.name = 123  # Should raise exception
    except Exception as e:
        print(f"Expected error for non-string name: {e}")
    
    # Test that hometown cannot be changed
    print(f"Band hometown (read-only): {band1.hometown}")
    # band1.hometown = "London"  # This would fail if uncommented
    
    return band1, venue1

def test_concert_creation():
    """Test creating concerts and relationships"""
    print("\nTesting concert creation...")
    
    band1 = Band("The Beatles", "Liverpool")
    venue1 = Venue("Cavern Club", "Liverpool")
    venue2 = Venue("Shea Stadium", "New York")
    
    # Create concerts
    concert1 = Concert("1962-08-01", band1, venue1)
    concert2 = Concert("1965-08-15", band1, venue2)
    
    print(f"Concert 1: {band1.name} at {venue1.name} on {concert1.date}")
    print(f"Concert 2: {band1.name} at {venue2.name} on {concert2.date}")
    
    # Test relationships
    print(f"\nBand concerts: {len(band1.concerts)} concerts")
    print(f"Venue1 concerts: {len(venue1.concerts)} concerts")
    print(f"Venue2 concerts: {len(venue2.concerts)} concerts")
    
    # Test venues for band
    print(f"\nVenues where {band1.name} played: {[v.name for v in band1.venues]}")
    
    # Test bands for venue
    print(f"Bands that played at {venue1.name}: {[b.name for b in venue1.bands]}")
    
    return band1, venue1, venue2, concert1, concert2

def test_methods():
    """Test the various methods"""
    print("\nTesting methods...")
    
    band1 = Band("The Beatles", "Liverpool")
    venue1 = Venue("Cavern Club", "Liverpool")
    venue2 = Venue("Shea Stadium", "New York")
    
    concert1 = Concert("1962-08-01", band1, venue1)
    concert2 = Concert("1965-08-15", band1, venue2)
    
    # Test hometown_show
    print(f"Concert at {venue1.name}: hometown show? {concert1.hometown_show()}")
    print(f"Concert at {venue2.name}: hometown show? {concert2.hometown_show()}")
    
    # Test introduction
    print(f"\nConcert introduction:")
    print(concert2.introduction())
    
    # Test play_in_venue method
    concert3 = band1.play_in_venue(venue1, "1963-03-01")
    print(f"\nNew concert created via play_in_venue: {concert3.date}")
    print(f"Band now has {len(band1.concerts)} concerts")
    
    # Test all_introductions
    print(f"\nAll introductions for {band1.name}:")
    for intro in band1.all_introductions():
        print(f"  - {intro}")
    
    # Test concert_on
    found_concert = venue1.concert_on("1962-08-01")
    print(f"\nConcert found on 1962-08-01 at {venue1.name}: {found_concert.date if found_concert else 'None'}")
    
    not_found = venue1.concert_on("1999-01-01")
    print(f"Concert found on 1999-01-01 at {venue1.name}: {'Found' if not_found else 'None'}")

def test_edge_cases():
    """Test edge cases and error handling"""
    print("\nTesting edge cases...")
    
    # Test with no concerts
    band2 = Band("New Band", "Seattle")
    venue3 = Venue("Empty Venue", "Portland")
    
    print(f"New band with no concerts: {band2.concerts}")
    print(f"New venue with no concerts: {venue3.concerts}")
    print(f"New band venues: {band2.venues}")
    print(f"New venue bands: {venue3.bands}")
    print(f"New band introductions: {band2.all_introductions()}")
    
    # Test property validations
    try:
        bad_concert = Concert("", band2, venue3)
    except Exception as e:
        print(f"\nExpected error for empty date: {e}")
    
    try:
        bad_concert = Concert("2023-01-01", "not a band", venue3)
    except Exception as e:
        print(f"Expected error for invalid band: {e}")
    
    try:
        bad_concert = Concert("2023-01-01", band2, "not a venue")
    except Exception as e:
        print(f"Expected error for invalid venue: {e}")

if __name__ == "__main__":
    print("=" * 50)
    print("Testing Concert Domain System")
    print("=" * 50)
    
    # Run tests
    test_initialization()
    test_concert_creation()
    test_methods()
    test_edge_cases()
    
    print("\n" + "=" * 50)
    print("All tests completed!")
    print("=" * 50)
    
    # Start ipdb session for manual testing
    import ipdb
    ipdb.set_trace()