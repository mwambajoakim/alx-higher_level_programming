-- Display top 3 cities temperature
SELECT city, value
FROM temperatures
WHERE month IN (7, 8)
ORDER BY value DESC
LIMIT 3;
