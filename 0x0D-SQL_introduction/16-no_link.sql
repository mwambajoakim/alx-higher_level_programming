-- Display all records except those without name
SELECT
  score, name
FROM
  second_table
WHERE
  name != NULL
ORDER BY
  score DESC;
