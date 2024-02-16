-- Script to list all cities of California
-- Find the state_id for California
USE hbtn_0d_usa;
SET @california_state_id := ( SELECT id FROM states WHERE name = 'California' LIMIT 1);
SELECT * FROM cities WHERE state_id = @california_state_id
ORDER BY id ASC;
