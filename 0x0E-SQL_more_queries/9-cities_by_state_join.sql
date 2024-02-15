-- Script to list all cities with their corresponding states
USE hbtn_0d_usa;
SELECT cities.id, cities.name, states.name AS state_name
FROM cities JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
