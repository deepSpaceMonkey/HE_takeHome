DROP TABLE IF EXISTS auction_results;
CREATE TABLE auction_results (
    result_id SERIAL PRIMARY KEY,
    participant_name TEXT NOT NULL,
    auction_unit TEXT NOT NULL,
    service_type TEXT NOT NULL,
    product_type TEXT NOT NULL,
    quantity_executed FLOAT,
    clearing_price NUMERIC,
    delivery_start TIMESTAMP NOT NULL,
    delivery_end TIMESTAMP NOT NULL,
    technology_type TEXT,
    post_code TEXT,
    unit_result_id TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP INDEX IF EXISTS idx_participant_name;
CREATE INDEX idx_participant_name ON auction_results (participant_name);

DROP INDEX IF EXISTS idx_auction_unit;
CREATE INDEX idx_auction_unit ON auction_results (auction_unit);

DROP INDEX IF EXISTS idx_delivery_period;
CREATE INDEX idx_delivery_period ON auction_results (delivery_start, delivery_end);
