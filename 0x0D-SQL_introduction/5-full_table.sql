-- information about table
-- information about a table using information schema db

-- SELECT * FROM information_schema.TABLES WHERE table_name = 'first_table';
SELECT DEFAULT_CHARACTER_SET_NAME, DEFAULT_COLLATION_NAME FROM INFORMATION_SCHEMA. SCHEMATA WHERE schema_name = "hbtn_0c_0";
