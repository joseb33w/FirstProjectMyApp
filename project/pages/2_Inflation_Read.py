import streamlit as st
import requests
import pandas as pd
from geopy.geocoders import Nominatim

# Set page configuration
st.set_page_config(page_title="Local Inflation", page_icon="📍", layout="wide")

# Function to fetch CPI data and calculate annual inflation rates
@st.cache_data
def get_annual_inflation(city, start_year, end_year, api_key):
    city_series_map = {
        "Dallas": "CUURA421SA0",  # CPI series for Dallas-Fort Worth-Arlington, TX
    }
    if city not in city_series_map:
        return None, None  # If the city is not in the series map
    
    series_id = city_series_map[city]
    url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
    payload = {
        "seriesid": [series_id],
        "startyear": str(start_year),
        "endyear": str(end_year),
        "registrationkey": api_key,
    }
    response = requests.post(url, json=payload, timeout=10)
    if response.status_code != 200:
        raise Exception(f"API request failed: {response.status_code}")
    
    data = response.json()
    if data["status"] != "REQUEST_SUCCEEDED":
        raise Exception("API request did not succeed.")
    
    series_data = data["Results"]["series"][0]["data"]
    cpi_values = {int(record["year"]): float(record["value"]) for record in series_data}

    # Sort CPI values by year
    cpi_values = dict(sorted(cpi_values.items()))
    
    # Calculate annual inflation rates
    inflation_rates = {}
    years = list(cpi_values.keys())
    for i in range(1, len(years)):
        current_year = years[i]
        previous_year = years[i - 1]
        inflation_rate = ((cpi_values[current_year] - cpi_values[previous_year]) / cpi_values[previous_year]) * 100
        inflation_rates[current_year] = inflation_rate
    
    return inflation_rates

# Function to get latitude and longitude for a location
@st.cache_data
def get_coordinates(location):
    geolocator = Nominatim(user_agent="streamlit-geolocator")
    location_data = geolocator.geocode(location)
    if location_data:
        return location_data.latitude, location_data.longitude
    else:
        return None, None

# Main function
def main():
    st.title("Search for Local Inflation Data")
    st.write("Search for a location on the map to view its inflation data (if available).")

    # Search bar
    location_input = st.text_input("Enter a location (e.g., Dallas, TX):", "Dallas, TX")

    # Fetch coordinates
    latitude, longitude = get_coordinates(location_input)

    # Display map with the searched location
    if latitude and longitude:
        map_data = pd.DataFrame({
            "latitude": [latitude],
            "longitude": [longitude]
        })
        st.map(map_data, zoom=6, use_container_width=True)
    else:
        st.error("Location not found. Please try again.")

    # Display inflation data if available
    if st.button("Get Inflation Data"):
        city_name = location_input.split(",")[0]  # Extract the city name
        start_year = 2000
        end_year = 2023
        api_key = "db3c57795ec542d4aca727c757f35799"  # Replace with your API key

        try:
            inflation_rates = get_annual_inflation(city_name, start_year, end_year, api_key)
            if inflation_rates:
                # Convert inflation rates to a DataFrame for visualization
                inflation_df = pd.DataFrame(list(inflation_rates.items()), columns=["Year", "Inflation Rate (%)"])
                inflation_df.set_index("Year", inplace=True)

                # Display bar chart
                st.subheader(f"Annual Inflation Rate for {city_name} (2000-2023)")
                st.bar_chart(inflation_df)
            else:
                st.warning(f"No inflation data available for {location_input}.")
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
