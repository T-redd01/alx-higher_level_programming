-- something here
-- something about goes here

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rate
FROM tv_shows
INNER JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rate DESC;
