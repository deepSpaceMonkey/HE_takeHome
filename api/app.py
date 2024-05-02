from data_fetching import fetch_data
from data_transforming import transform_data
from data_storing import insert_data_into_db
import pandas as pd


def main():
    # Fetch and process data
    df, current_date = fetch_data()
    if df.empty or current_date is None:
        print("Failed to fetch data or get current date.")
        return

    df = transform_data(df)
    print("Before filtering, DataFrame shape:", df.shape)

    # Filter data to include only today's data
    df['delivery_start'] = pd.to_datetime(df['delivery_start']).dt.date
    df_filtered = df[df['delivery_start'] == current_date]

    print("After filtering, DataFrame shape:", df_filtered.shape)
    if df_filtered.empty:
        print("No data to insert. DataFrame is empty after filtering.")
    else:
        print("Transformed DataFrame ready for insertion:")
        insert_data_into_db(df_filtered)
        print("Data successfully inserted into database.")


if __name__ == "__main__":
    main()
