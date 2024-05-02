DROP TABLE IF EXISTS auction_results;
CREATE TABLE auction_results (
    result_id INTEGER PRIMARY KEY,
    registered_auction_participant TEXT NOT NULL,
    auction_unit TEXT NOT NULL,
    service_type TEXT NOT NULL,
    product_type TEXT NOT NULL,
    quantity_executed FLOAT,
    clearing_price NUMERIC,
    delivery_start TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    delivery_end TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    technology_type TEXT,
    post_code TEXT,
    unit_result_id TEXT NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    full_text TEXT
);

-- Indices to improve query performance based on common search columns
DROP INDEX IF EXISTS idx_participant_name;
CREATE INDEX idx_participant_name ON auction_results (registered_auction_participant);

DROP INDEX IF EXISTS idx_auction_unit;
CREATE INDEX idx_auction_unit ON auction_results (auction_unit);

DROP INDEX IF EXISTS idx_delivery_period;
CREATE INDEX idx_delivery_period ON auction_results (delivery_start, delivery_end);
