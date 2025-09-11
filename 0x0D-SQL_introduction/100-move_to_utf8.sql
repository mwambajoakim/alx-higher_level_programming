-- Converts a database to UTF-8
ALTER DATABASE
  hbtn_0c_0
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

ALTER TABLE
  first_table
CONVERT TO CHARACTER SET
  utf8mb4
COLLATE
  utf8mb4_unicode_ci;

ALTER TABLE first_table
COLUMN name
CONVERT TO CHARACTER SET
  utf8mb
COLLATE
  utf8mb_unicode_ci;
