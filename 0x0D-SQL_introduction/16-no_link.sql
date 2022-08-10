-- Query to list all the records in the second_table who have a name value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
