-- Script to list all genres and the number of shows linked to each
-- List all genres and the number of shows linked to each
USE hbtn_0d_tvshows;
SELECT tv_show_genres.genre_id AS genre,
COUNT(tv_shows.id) AS number_of_shows FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
