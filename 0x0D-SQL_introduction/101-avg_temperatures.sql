-- finding average per city
-- working with real data to find average

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC; 
