-- display only top 3
-- display top 3 temps forjuly and august

SELECT city, AVG(value) AS avg_temp FROM  temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3; 
