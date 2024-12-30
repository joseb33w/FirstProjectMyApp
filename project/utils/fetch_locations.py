import sqlite3
from geopy.geocoders import Nominatim

# Create or connect to the database
conn = sqlite3.connect("locations.db")
cursor = conn.cursor()

# Create the table for storing locations
cursor.execute("""
    CREATE TABLE IF NOT EXISTS locations (
        name TEXT PRIMARY KEY,
        latitude REAL,
        longitude REAL
    )
""")
conn.commit()

# Function to fetch and store location data
def fetch_and_store_location(location_name):
    geolocator = Nominatim(user_agent="streamlit-app")
    location = geolocator.geocode(location_name)
    if location:
        cursor.execute(
            "INSERT OR IGNORE INTO locations (name, latitude, longitude) VALUES (?, ?, ?)",
            (location_name, location.latitude, location.longitude)
        )
        conn.commit()
        return location.latitude, location.longitude
    return None, None

# Pre-fetch locations (Add more as needed)
fetch_and_store_location("Dallas, TX")
fetch_and_store_location("Austin, TX")
fetch_and_store_location("Houston, TX")
fetch_and_store_location("San Antonio, TX")
conn.close()
