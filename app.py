import streamlit as st
from process_flight_data import process_flight_data

data = '''Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21,40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22,87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12,33];20055.0;london_MONTreal\n'''


st.title("Flight Data Table")
st.write("Flight Data")

df = process_flight_data(data)
st.dataframe(df)

csv = df.to_csv(index=False)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name="flight_data.csv",
    mime="text/csv",
)