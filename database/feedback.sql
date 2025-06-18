-- Create database
CREATE DATABASE IF NOT EXISTS feedback;

-- Use the database
USE feedback;

-- Create table with correct column names
CREATE TABLE IF NOT EXISTS feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100),
    email VARCHAR(100),
    comment TEXT,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
