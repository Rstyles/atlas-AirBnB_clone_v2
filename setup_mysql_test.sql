-- Creates a test bd
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test' @'localhost' IDENTIFIED BY 'hbnb_test_pwd';
REVOKE ALL PRIVILEGES ON *.*
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test' @'localhost';
FROM 'hbnb_test' @'localhost';
GRANT SELECT ON hbnb_test_db.* TO 'hbnb_test' @'localhost';