-- Display max temperature by state

SELECT state MAX(value) AS max_temp
FROM temperatures
ORDER BY state;
