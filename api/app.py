import pandas as pd
import requests
from sqlalchemy import create_engine


def main():
    sql_query = '''SELECT * FROM "a63ab354-7e68-44c2-ad96-c6f920c30e85" ORDER BY "_id" ASC LIMIT 100'''
    params = {'sql': sql_query}

    try:
        response = requests.get('https://api.nationalgrideso.com/api/3/action/datastore_search_sql', params=params)
        response.raise_for_status()
        data = response.json()["result"]
        df = pd.DataFrame(data["records"])
        df = transform_data(df)
        print("Transformed DataFrame ready for insertion:")

        # Database connection settings
        database_url = "postgresql://postgres:postgres@db:5432/postgres"  # Adjust as needed
        insert_data_into_db(df, database_url)
        print("Data successfully inserted into database.")
    except requests.exceptions.RequestException as e:
        print(str(e))
    except Exception as e:
        print(f"An error occurred: {e}")


def transform_data(df):
    column_map = {
        "registeredAuctionParticipant": "participant_name",
        "auctionUnit": "auction_unit",
        "serviceType": "service_type",
        "auctionProduct": "product_type",
        "executedQuantity": "quantity_executed",
        "clearingPrice": "clearing_price",
        "deliveryStart": "delivery_start",
        "deliveryEnd": "delivery_end",
        "technologyType": "technology_type",
        "postCode": "post_code",
        "unitResultID": "unit_result_id"
    }
    df.rename(columns=column_map, inplace=True)
    return df


def insert_data_into_db(df, database_url):
    engine = create_engine(database_url)
    df.to_sql('auction_results', con=engine, if_exists='append', index=False)
    engine.dispose()  # Close the connection


if __name__ == "__main__":
    main()
