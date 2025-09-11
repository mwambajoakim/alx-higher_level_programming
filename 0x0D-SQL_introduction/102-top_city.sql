-- Display top 3 cities temperature
SELECT city, value
FROM temperatures
WHERE month = 1 and month = 2
ORDER BY value DESC LIMIT 3;
