CREATE DATABASE delivery_system;
USE delivery_system;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    address VARCHAR(255),
    status VARCHAR(50),
    customer_email VARCHAR(100)
);