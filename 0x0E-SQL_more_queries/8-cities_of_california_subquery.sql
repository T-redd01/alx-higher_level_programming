-- LISTING ONLY CERTAIN CITIES
-- listing ities by name

SELECT id, state_id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
