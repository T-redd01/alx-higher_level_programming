-- LISTING ONLY CERTAIN CITIES
-- listing ities by name

SELECT *
FROM cities
WHERE id = (SELECT id FROM states WHERE 'name' = 'California')
ORDER BY id ASC;
