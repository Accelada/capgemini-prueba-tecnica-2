CREATE TABLE IF NOT EXISTS results (
    id SERIAL PRIMARY KEY,
    val INTEGER NOT NULL,
    val_squared BIGINT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);