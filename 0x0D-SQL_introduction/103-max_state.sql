-- max temp per state
-- retrieving max temp per state

SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
