-- Lists all cities contained in the database hbtn_0d_usa.

SELECT cities.id, cities.name
FROM cities
INNER JOIN states.name
ON cities.state_id = states.id
ORDER BY cities.id ASC;
