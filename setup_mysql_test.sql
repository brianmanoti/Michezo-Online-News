-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS Michezo-Online-News;
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin_pwd';
GRANT ALL PRIVILEGES ON `Michezo-Online-News`.* TO 'admin'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;
