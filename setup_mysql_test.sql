-- Creates a test bd

CREATE DATABASE IF NOT EXISTS hbtn_test_db;

CREATE USER IF NOT EXISTS 'hbtn_user'@'localhost' IDENTIFIED BY 'hbtn_pass';

GRANT ALL PRIVILEGES ON hbtn_test_db.* TO 'hbtn_user'@'localhost';

GRANT SELECT ON hbtn_test_db.* TO 'hbtn_user'@'localhost';

FLUSH PRIVILEGES;