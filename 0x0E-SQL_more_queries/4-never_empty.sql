-- Script to create the table id_not_null
-- Create table id_not_null if it doesn't exist
CREATE TABLE IF NOT EXISTS
	id_not_null ( id INT DEFAULT 1, name VARCHAR(256), PRIMARY KEY (id));
FLUSH PRIVILEGES;
