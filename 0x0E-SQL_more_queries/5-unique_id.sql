-- Script to create the table unique_id
-- Create table unique_id if it doesn't exist
CREATE TABLE IF NOT EXISTS
	unique_id (
		id INT DEFAULT 1 UNIQUE,
		name VARCHAR(256),
		PRIMARY KEY (id)
	);
FLUSH PRIVILEGES;
