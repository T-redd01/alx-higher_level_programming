-- list specific records
-- list only score and name that is not null

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
