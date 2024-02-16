-- Create table force_name if it doesn't exist
USE your_database;
CREATE TABLE IF NOT EXISTS force_name (
	id INT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id));
FLUSH PRIVILEGES;
