-- Creates a test bd

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbtn_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbtn_user'@'localhost';

GRANT SELECT ON hbnb_test_db.* TO 'hbtn_user'@'localhost';

FLUSH PRIVILEGES;