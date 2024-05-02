import pandas as pd
import requests
from sqlalchemy import create_engine
import pytz
from datetime import datetime

def main():
    # Get the current date in CT timezone
    ct_timezone = pytz.timezone('America/Chicago')
    current_date = datetime.now(ct_timezone).date()  # this gets the date part only
    print("Current date (CT):", current_date)

    # Fetch all records
    # TODO: adjust query to only get data from current date
    sql_query = f'''SELECT * FROM "a63ab354-7e68-44c2-ad96-c6f920c30e85" ORDER BY "_id" ASC'''
    params = {'sql': sql_query}

    try:
        response = requests.get('https://api.nationalgrideso.com/api/3/action/datastore_search_sql', params=params)
        response.raise_for_status()
        data = response.json()["result"]
        df = pd.DataFrame(data["records"])
        df = transform_data(df)

        # Debug print before filtering
        print("Before filtering, DataFrame shape:", df.shape)

        # Filter DataFrame based on the 'delivery_start' matching today's date
        df['delivery_start'] = pd.to_datetime(df['delivery_start']).dt.date
        df_filtered = df[df['delivery_start'] == current_date]

        print("After filtering, DataFrame shape:", df_filtered.shape)
        if df_filtered.empty:
            print("No data to insert. DataFrame is empty after filtering.")
        else:
            print("Transformed DataFrame ready for insertion:")
            database_url = "postgresql://postgres:postgres@db:5432/postgres"
            insert_data_into_db(df_filtered, database_url)
            print("Data successfully inserted into database.")
    except requests.exceptions.RequestException as e:
        print(str(e))
    except Exception as e:
        print(f"An error occurred: {e}")

def transform_data(df):
    column_map = {
        "_id": "result_id",
        "registeredAuctionParticipant": "registered_auction_participant",
        "auctionUnit": "auction_unit",
        "serviceType": "service_type",
        "auctionProduct": "product_type",
        "executedQuantity": "quantity_executed",
        "clearingPrice": "clearing_price",
        "deliveryStart": "delivery_start",
        "deliveryEnd": "delivery_end",
        "technologyType": "technology_type",
        "postCode": "post_code",
        "unitResultID": "unit_result_id",
        "_full_text": "full_text"
    }
    df.rename(columns=column_map, inplace=True)
    return df

def insert_data_into_db(df, database_url):
    try:
        engine = create_engine(database_url)
        print("Columns being inserted:", df.columns)  # Debugging
        df.to_sql('auction_results', con=engine, if_exists='append', index=False)
        print("Rows inserted:", len(df))
    except Exception as e:
        print(f"General error: {e}")
    finally:
        engine.dispose()

if __name__ == "__main__":
    main()
