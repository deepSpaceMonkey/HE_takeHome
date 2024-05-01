# Install pandas package if you don't have it already
# pip install pandas

# Get data and convert into dataframe
import pandas as pd
import requests
from urllib import parse

sql_query = '''SELECT * FROM  "a63ab354-7e68-44c2-ad96-c6f920c30e85" ORDER BY "_id" ASC LIMIT 100'''
params = {'sql': sql_query}

try:
    resposne = requests.get('https://api.nationalgrideso.com/api/3/action/datastore_search_sql', params = parse.urlencode(params))
    data = resposne.json()["result"]
    df = pd.DataFrame(data["records"])
    print(df) # Dataframe
except requests.exceptions.RequestException as e:
    print(e.response.text)