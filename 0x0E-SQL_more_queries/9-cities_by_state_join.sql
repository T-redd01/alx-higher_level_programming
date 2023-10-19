-- trying joins
-- joining from cities and states

SELECT id, name FROM cities OUTER JOIN states.name ON cities.state_id = state.id;
