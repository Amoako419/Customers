-- Create the users table
CREATE TABLE IF NOT EXISTS users (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);