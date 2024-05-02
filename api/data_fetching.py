import requests
import pandas as pd
from config import CT_TIMEZONE
from datetime import datetime


def fetch_data():
    # Get the current date in Central Time
    current_date = datetime.now(CT_TIMEZONE).date()  # this gets the date part only
    print("Current date (CT):", current_date)

    # SQL query to fetch data
    sql_query = f'''SELECT * FROM "a63ab354-7e68-44c2-ad96-c6f920c30e85" ORDER BY "_id" ASC'''
    params = {'sql': sql_query}
    try:
        # Make HTTP request to fetch data
        response = requests.get('https://api.nationalgrideso.com/api/3/action/datastore_search_sql', params=params)
        response.raise_for_status()
        data = response.json()["result"]
        df = pd.DataFrame(data["records"])
        return df, current_date
    except requests.exceptions.RequestException as e:
        print(str(e))
        return pd.DataFrame(), None # return empty dataframe and none if error occurs
