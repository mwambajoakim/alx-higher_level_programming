-- import table to hbtn_0c_0
mysql -u root -p hbtn_0c_0 < temperatures.sql

SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
