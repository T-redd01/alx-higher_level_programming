-- more multi joins
-- movie names and genre names

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres
ON tv_genre.id = tv_show_genre.genre_id
ORDER BY tv_shows.title, tv_genres.name ASC;
