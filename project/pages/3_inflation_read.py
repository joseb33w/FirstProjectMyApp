import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch CPI data and calculate inflation rate with caching
@st.cache
def get_cpi_data(location, start_year, end_year, api_key):
    location_series_map = {
        "Dallas": "CUURA421SA0",  # CPI for Dallas-Fort Worth-Arlington, TX
    }
    if location not in location_series_map:
        raise ValueError(f"Location '{location}' is not supported.")
    
    series_id = location_series_map[location]
    url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
    payload = {
        "seriesid": [series_id],
        "startyear": str(start_year),
        "endyear": str(end_year),
        "registrationkey": api_key,
    }
    response = requests.post(url, json=payload, timeout=10)  # Added timeout
    if response.status_code != 200:
        raise Exception(f"API request failed: {response.status_code}")
    
    data = response.json()
    if data["status"] != "REQUEST_SUCCEEDED":
        raise Exception("API request did not succeed.")
    
    series_data = data["Results"]["series"][0]["data"]
    cpi_values = {}
    for record in series_data:
        year = int(record["year"])
        if year in {start_year, end_year}:
            cpi_values[year] = float(record["value"])
    
    inflation_rate = ((cpi_values[end_year] - cpi_values[start_year]) / cpi_values[start_year]) * 100
    return cpi_values, inflation_rate

# Main function
def main():
    st.title("Inflation Visualizer")
    location = st.selectbox("Select a Location:", ["Dallas"])
    start_year = st.number_input("Start Year:", min_value=2000, max_value=2023, value=2020)
    end_year = st.number_input("End Year:", min_value=2000, max_value=2023, value=2023)
    api_key = "db3c57795ec542d4aca727c757f35799"  # Integrated API key

    if st.button("Calculate Inflation"):
        try:
            cpi_values, inflation_rate = get_cpi_data(location, start_year, end_year, api_key)
            st.subheader(f"Inflation Rate in {location} ({start_year} - {end_year}):")
            st.write(f"**{inflation_rate:.2f}%**")
            cpi_df = pd.DataFrame({"Year": [start_year, end_year], "CPI": [cpi_values[start_year], cpi_values[end_year]]})
            st.bar_chart(cpi_df.set_index("Year"))
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
