# Flight Data Processor


## Overview
Data Platform Team Co-op Case Study - Solution
The task involves cleaning 'Airline Code' by removing punctuation, splitting 'To_From' into 'To' and 'From' with uppercase formatting, and filling missing 'FlightCodes' with a +10 increment, converting to integers using SQL. The solution includes process_flight_data.py for data processing and app.py for a Streamlit visualization. Hope you will like it :)

![Preview](./preview.png)

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
- CSV download


## Notes
- Data includes airline codes, delay times, flight codes, and routes
- Ensures consistent airline naming ("Air France 12" -> "Air France")
