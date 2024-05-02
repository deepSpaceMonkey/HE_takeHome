import pandas as pd
import requests

def main():
    sql_query = '''SELECT * FROM "a63ab354-7e68-44c2-ad96-c6f920c30e85" ORDER BY "_id" ASC LIMIT 100'''
    params = {'sql': sql_query}

    try:
        response = requests.get('https://api.nationalgrideso.com/api/3/action/datastore_search_sql', params=params)
        response.raise_for_status()  # Raises stored HTTPError, if one occurred.
        data = response.json()["result"]
        df = pd.DataFrame(data["records"])
        df = transform_data(df)
        print(df)  # Dataframe
    except requests.exceptions.RequestException as e:
        print(str(e))

def transform_data(df):
    # Map columns directly within the DataFrame
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
    # Rename the columns based on the mapping
    df.rename(columns=column_map, inplace=True)
    return df

if __name__ == "__main__":
    main()
