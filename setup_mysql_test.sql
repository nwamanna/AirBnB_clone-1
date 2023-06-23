-- Setting up my database

-- Create a database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant user all privilege on the database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Apply all change
FLUSH PRIVILEGES;
