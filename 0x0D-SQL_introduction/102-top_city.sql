-- Display top 3 cities temperature
SELECT city, value AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
ORDER BY avg_temp DESC
LIMIT 3;
