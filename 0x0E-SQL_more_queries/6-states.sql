-- Script to create the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create table states if it doesn't exist
CREATE TABLE IF NOT EXISTS
	states (
		id INT AUTO_INCREMENT PRIMARY KEY,
		name VARCHAR(256) NOT NULL
);
FLUSH PRIVILEGES;
