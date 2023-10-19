-- genres for one show
-- find all genres that one show has

SELECT name
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.show_id = (
	SELECT DISTINCT show_id
	FROM tv_show_genres
	INNER JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_shows.title = 'Dexter'
)
ORDER BY name
;
