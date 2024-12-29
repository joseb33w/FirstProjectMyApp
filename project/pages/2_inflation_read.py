import streamlit as st
import requests
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Local Inflation", page_icon="🏙️", layout="wide")

# Function to fetch CPI data and calculate inflation rate
@st.cache_data
def get_cpi_data(city, start_year, end_year, api_key):
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
    cpi_values = {}
    for record in series_data:
        year = int(record["year"])
        if year in {start_year, end_year}:
            cpi_values[year] = float(record["value"])
    
    inflation_rate = ((cpi_values[end_year] - cpi_values[start_year]) / cpi_values[start_year]) * 100
    return cpi_values, inflation_rate

# Main function
def main():
    st.title("Local Inflation")
    st.write("This page displays local inflation data for Dallas, TX.")

    # Inputs
    city = "Dallas"
    start_year = st.number_input("Start Year:", min_value=2000, max_value=2023, value=2020)
    end_year = st.number_input("End Year:", min_value=2000, max_value=2023, value=2023)
    api_key = "db3c57795ec542d4aca727c757f35799"  # Replace with your actual API key

    # Fetch and display results
    if st.button("Get Inflation Data"):
        try:
            cpi_values, inflation_rate = get_cpi_data(city, start_year, end_year, api_key)
            
            # Display results
            st.subheader(f"Inflation Rate in {city} ({start_year} - {end_year}):")
            st.write(f"**{inflation_rate:.2f}%**")
            
            # Show CPI values as a bar chart
            cpi_df = pd.DataFrame({"Year": [start_year, end_year], "CPI": [cpi_values[start_year], cpi_values[end_year]]})
            st.bar_chart(cpi_df.set_index("Year"))
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
