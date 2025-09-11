-- Display top 3 cities temperature
SELECT city, value AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
ORDER BY avg_temp DESC
LIMIT 3;
