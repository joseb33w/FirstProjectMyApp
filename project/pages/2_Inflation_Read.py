import streamlit as st
import requests
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Local Inflation", page_icon="🏙️", layout="wide")

# Function to fetch CPI data and calculate annual inflation rates
@st.cache_data
def get_annual_inflation(city, start_year, end_year, api_key):
    city_series_map = {
        "Dallas": "CUURA421SA0"  # CPI series for Dallas-Fort Worth-Arlington, TX
    }
    if city not in city_series_map:
        raise ValueError(f"City '{city}' is not supported.")
    
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

# Main function
def main():
    st.title("Local Inflation: Dallas, TX")
    st.write("This page displays the annual inflation rate for Dallas, TX, and includes an interactive map.")

    # Fixed range of years for inflation data
    start_year = 2000
    end_year = 2023
    api_key = "db3c57795ec542d4aca727c757f35799"  # Replace with your actual API key

    # Map Data
    map_data = pd.DataFrame({
        "latitude": [32.7767],  # Latitude of Dallas
        "longitude": [-96.7970]  # Longitude of Dallas
    })

    # Display map
    st.map(map_data, zoom=6, use_container_width=True)
    st.write("Click on the location of Dallas in the map above to view its inflation data.")

    # Simulate a user click for Dallas's location
    if st.button("View Inflation Data for Dallas"):
        try:
            inflation_rates = get_annual_inflation("Dallas", start_year, end_year, api_key)
            
            # Convert inflation rates to a DataFrame for visualization
            inflation_df = pd.DataFrame(list(inflation_rates.items()), columns=["Year", "Inflation Rate (%)"])
            inflation_df.set_index("Year", inplace=True)
            
            # Display bar chart
            st.subheader("Annual Inflation Rate for Dallas, TX (2000-2023)")
            st.bar_chart(inflation_df)
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
