-- joining tables
-- join movie names with genre id

SELECT title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN hbtn_0d_tvshows.tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title ASC;
