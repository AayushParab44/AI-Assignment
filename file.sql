-- I ran this code on mysql workbench 

CREATE DATABASE your_database_name;
use your_database_name;

CREATE TABLE prediction_logs (
    image_path VARCHAR(255),
    predictions TEXT
);
