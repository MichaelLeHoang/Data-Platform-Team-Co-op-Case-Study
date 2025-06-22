# Flight Data Processor

## Overview
Data Platform Team Co-op Case Study

## Files
- `process_flight_data.py`: Cleans and processes flight data into a DataFrame.
- `app.py`: Streamlit app to visualize the data.
- `requirements.txt`: Dependencies list.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `streamlit run app.py`

## Features
- Cleans airline codes, parses delay times, and fills missing flight codes.
- Displays data in an interactive table.
- Offers CSV download.


## Notes
- Data includes airline codes, delay times, flight codes, and routes.
- Ensures consistent airline naming (e.g., "Air France 12").