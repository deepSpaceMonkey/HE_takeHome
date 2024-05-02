from sqlalchemy import create_engine
from config import DATABASE_URL


def insert_data_into_db(df):
    try:
        # Create SQLAlchemy Engine to connect to the PostgreSQL database
        engine = create_engine(DATABASE_URL)
        print("Columns being inserted:", df.columns)  # Debugging
        df.to_sql('auction_results', con=engine, if_exists='append', index=False)
        print("Rows inserted:", len(df))
    except Exception as e:
        print(f"General error: {e}")
    finally:
        # Close the engine
        engine.dispose()
