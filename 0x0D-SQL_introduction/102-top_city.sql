-- Display top 3 cities temperature
SELECT city, value
FROM temperatures
WHERE month = 1 and month = 2
LIMIT 3
ORDER BY value DESC;
