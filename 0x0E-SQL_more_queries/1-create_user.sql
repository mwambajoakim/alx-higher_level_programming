-- Create a user user_0d_1
-- Sets the password
-- Grants all privileges to user

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
       IDENTIFIED BY 'User123!';

GRANT ALL PRIVILEGES ON *.*
      TO 'user_0d_1'@'localhost';

FLUSH PRIVILEGES;
