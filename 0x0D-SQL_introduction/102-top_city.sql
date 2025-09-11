-- Display top 3 cities temperature
SELECT city, value
FROM temperatures
WHERE month = 7 and month = 8
LIMIT 3
ORDER BY value DESC;
