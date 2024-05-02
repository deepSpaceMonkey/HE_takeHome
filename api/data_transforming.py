def transform_data(df):
    # Create mapping from json input to database column names
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
