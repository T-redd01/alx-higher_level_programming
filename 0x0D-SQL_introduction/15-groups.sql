-- list number of same records
-- groups same numbers ad counts them

SELECT score, COUNT(*) AS number FROM second_table GROUP BY number ORDER BY DESC;
