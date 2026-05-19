CREATE DATABASE flight_db;
USE flight_db;
CREATE TABLE passengers (username VARCHAR(50) PRIMARY KEY,password VARCHAR(50));
CREATE TABLE tickets (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    flight_name VARCHAR(50),
    source VARCHAR(50),
    destination VARCHAR(50),
    status VARCHAR(20)
);
