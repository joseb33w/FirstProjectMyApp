import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_cpi_data(location, start_year, end_year, api_key):
    """
    Fetches CPI data for a specific location and calculates inflation rate.
    """
    # Map location to a BLS series ID
    location_series_map = {
        "Dallas": "CUURA421SA0",  # CPI for Dallas-Fort Worth-Arlington, TX
        # Add more locations and their series IDs here
    }
    
    if location not in location_series_map:
        raise ValueError(f"Location '{location}' is not supported.")
    
    series_id = location_series_map[location]
    url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
    
    headers = {"Content-Type": "application/json"}
    payload = {
        "seriesid": [series_id],
        "startyear": str(start_year),
        "endyear": str(end_year),
        "registrationkey": api_key,
    }
    
    # Fetch data from the BLS API
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
    
    data = response.json()
    if data["status"] != "REQUEST_SUCCEEDED":
        raise Exception("API request did not succeed.")
    
    # Extract CPI values
    series_data = data["Results"]["series"][0]["data"]
    cpi_values = {}
    for record in series_data:
        year = int(record["year"])
        if year == start_year or year == end_year:
            cpi_values[year] = float(record["value"])
    
    if start_year not in cpi_values or end_year not in cpi_values:
        raise Exception("CPI data for the specified years is unavailable.")
    
    # Calculate inflation rate
    inflation_rate = ((cpi_values[end_year] - cpi_values[start_year]) / cpi_values[start_year]) * 100
    return cpi_values, inflation_rate

# Streamlit app
st.set_page_config(page_title="Inflation Visualizer", page_icon="📊")

st.title("Inflation Visualizer")

# Inputs
location = st.selectbox("Select a Location:", ["Dallas"])
start_year = st.number_input("Start Year:", min_value=2000, max_value=2023, value=2020, step=1)
end_year = st.number_input("End Year:", min_value=2000, max_value=2023, value=2023, step=1)

# Integrated API key
API_KEY = "db3c57795ec542d4aca727c757f35799"

if st.button("Calculate Inflation"):
    try:
        cpi_values, inflation_rate = get_cpi_data(location, start_year, end_year, API_KEY)
        
        # Display results
        st.subheader(f"Inflation Rate in {location} ({start_year} - {end_year}):")
        st.write(f"**{inflation_rate:.2f}%**")
        
        # Create a bar chart
        cpi_df = pd.DataFrame({
            "Year": [start_year, end_year],
            "CPI": [cpi_values[start_year], cpi_values[end_year]]
        })
        
        fig, ax = plt.subplots()
        ax.bar(cpi_df["Year"].astype(str), cpi_df["CPI"], color=["blue", "orange"])
        ax.set_title(f"CPI Comparison ({start_year} vs {end_year})")
        ax.set_ylabel("CPI")
        ax.set_xlabel("Year")
        st.pyplot(fig)
    
    except Exception as e:
        st.error(f"Error: {e}")
