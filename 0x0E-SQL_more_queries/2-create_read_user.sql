-- Create database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

--Create user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
       IDENTIFIED BY 'user_0d_2_pwd';

-- Give user user_0d_2_pwd select privilege
GRANT SELECT ON hbtn_0d_2 TO 'user_od_2'@'localhost';
