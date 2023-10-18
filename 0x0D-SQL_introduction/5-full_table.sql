-- information about table
-- information about a table using information schema db

SELECT table_name, create_table FROM information_schema.TABLES WHERE table_name = 'first_table';
