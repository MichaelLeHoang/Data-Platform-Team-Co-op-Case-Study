import re
import pandas as pd
from ast import literal_eval


def process_flight_data(data: str) -> pd.DataFrame:
    """
    Parse, clean and normalize a semicolon-delimited flight data string into a pandas DataFrame

    Args:
        data (str): Raw multi-line string of form
                    "Airline Code;DelayTimes;FlightCodes;To_From…", 
                    where DelayTimes is a list literal and FlightCodes may be blank

    Returns:
        pandas.DataFrame: Cleaned table with correct types and no missing flight codes

    """ 

    lines = data.strip().split('\n')
    headers = lines[0].split(';')
    rows = [line.split(';') for line in lines[1:]]

    # clean Airline Code
    airline_clean = lambda s: ' '.join(w for w in re.sub(r'[^\w\s]', '', s).split() 
                                       if not w.isdigit()
                                       ).strip().title()

    # make DalayTimes from string list to actual list
    parse_delays  = lambda s: literal_eval(s) if s.strip() else []

    # extract Flight Code, required to be interger instead of float
    flight_codes = []
    for airline, delays, fc, to_from in rows:
        if fc.strip():
            flight_codes.append(int(float(fc)))
        else:
            flight_codes.append(None)

    # for the one that does not have flight code (or None), we will fill
    #       in missing codes by linearly stepping by +10
    has_flight_codes = [fc for fc in flight_codes if fc is not None]
    start = has_flight_codes[0]
    full_codes = list(range(start, start + len(rows) * 10, 10))
    for i in range(len(flight_codes)):
        if flight_codes[i] is None:
            flight_codes[i] = full_codes[i]

    # split To_From to two separates columns
    to_list, from_list = [], []
    for _, _, _, to_from in rows:
        a, b = to_from.split('_')
        to_list.append(a.title())
        from_list.append(b.title())

    # finally! putting everything together in the table
    cleaned = []
    for i, row in enumerate(rows):
        airline_uncleaned, delays_uncleaned, _, _ = row
        cleaned.append({
            'Airline Code': airline_clean(airline_uncleaned),
            'DelayTimes': parse_delays(delays_uncleaned),
            'FlightCode': flight_codes[i],
            'To': to_list[i],
            'From': from_list[i],
        })
    
    return pd.DataFrame(cleaned)

data = '''Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21,40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22,87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12,33];20055.0;london_MONTreal\n'''

if __name__ == "__main__":
    df = process_flight_data(data)
    print(df)