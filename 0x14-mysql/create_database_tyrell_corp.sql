-- Create the tyrell_corp database
-- Switch to the tyrell_corp database
place column_name with actual column names)
-- Create the nexus6 table with appropriate columns (replace column_name with actual column names)
CREATE DATABASE tyrell_corp;
USE tyrell_corp;
CREATE TABLE nexus6 (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255)
);
-- Insert at least one entry into the nexus6 table (replace values with actual data)

INSERT INTO nexus6 (name) VALUES ('Leon');

-- Grant SELECT permissions on the nexus6 table to the 
holberton_user
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;

-- Exit MySQL
EXIT;
