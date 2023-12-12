# AI Assignment
This repository contains a Flask web application with a MySQL database backend. The application includes a machine learning model using PyTorch.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Application Structure](#application-structure)
- [Usage](#usage)

## Prerequisites
These are required to be installed on the machine:
- Git
- Python
- MySQL Database and Workbench

## Getting Started
1. Clone this repository:

   git clone https://github.com/AayushParab44/AI-Assignment.git

2. Navigate to the project directory:
   cd (name of project directory)
   Example: cd AI-Assignment

3. Install Python dependencies:

   pip install -r requirements.txt

4. Set up your MySQL database:
   Create a database with a name and a password.

5. Update 'password' and 'database' variables on line 29 and 30 in 'final_app.py' file according to those set for the database in step 4.

6. Run the Flask application:
   python final_app.py
   Access the web application at http://127.0.0.1:5000/

## Application Structure

The application is structured as follows:

- **templates/:** Stores HTML templates for the web application.
- **test_images/:** Directory for test images used by the application.
- **final_app.py:** The main script for running the Flask app.
- **requirements.txt:** Lists Python dependencies for the Flask app.
- **file.sql:** Contains SQL code to create the database.
- **MNIST_with_pytorch.ipynb:** Contains code to create, train, and save the model. I had run this notebook on Google Colab.
- **my_model.pth:** The MNIST model.
- **docker-compose.yml, Dockerfile:** The Docker files.

## Usage

    Access the web application at http://127.0.0.1:5000/
    
    Upload an image from the 'test_images' folder in the repository and click on upload button. The predicted value will be shown on the screen as well as will be updated in the database table.   

