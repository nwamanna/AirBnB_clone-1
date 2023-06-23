-- Setting up my database

-- Create a database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant user all privilege on the database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply all change
FLUSH PRIVILEGES;
