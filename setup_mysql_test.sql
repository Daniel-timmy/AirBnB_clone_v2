--Prepares a MySQL server
-- create project developement database with the name : hbnb_test_db

CREATE DATABASE IF NOT EXIST hbnb_test_db;
CREATE USER IF NOT EXIST 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;