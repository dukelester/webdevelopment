# webdevelopement Projects

This repository contains multiple web development projects built with different technologies such as Python, Flask, FastAPI, Node.js, Express.js, React.js, JavaScript, SQL, PostgreSQL, and more.

Each project has its own directory within this repository, with a separate README file detailing the project's purpose, usage, and technologies used.

## Projects

### Project Name 1: Flask Web Application

This project is a web application built with Python and Flask, and it aims to create a web application that allows users to create, read, update, and delete items from a database. The application has an authentication system to manage user accounts and secure access to the data.

#### Technologies Used:

- Python
- Flask
- SQLAlchemy
- WTForms
- Flask-Login
- HTML/CSS/JS

#### Usage:

1. Clone the repository to your local machine:
git clone https://github.com/dukelester/webdevelopement.git

2. Navigate to the project directory:

cd webdevelopement/project-1

3. Install the dependencies:

pip install -r requirements.txt

4. Set up the database by running the following commands:

flask db init
flask db migrate
flask db upgrade

5. Start the web application:

flask run

6. Open your web browser and navigate to `http://localhost:5000` to access the web application.

### Project Name 2: Express.js RESTful API

This project is a RESTful API built with Node.js and Express.js, and it aims to create an API that provides CRUD operations for managing a list of products. The API is secured with JSON Web Tokens (JWT) authentication and uses a PostgreSQL database to store the data.

#### Technologies Used:

- Node.js
- Express.js
- PostgreSQL
- JSON Web Tokens (JWT)
- Bcrypt
- Knex.js

#### Usage:

1. Clone the repository to your local machine:
git clone https://github.com/dukelester/webdevelopement.git

2. Navigate to the project directory:
cd webdevelopement/project-2

3. Install the dependencies:

npm install

4. Set up the database by running the following commands:

psql -f setup.sql

5. Start the API:

npm start

6. Use a tool like Postman to make requests to the API.

## Conclusion

This repository provides a variety of web development projects built with different technologies, and it can serve as a valuable resource for learning and practicing web development. Each project has its own README file with detailed instructions on how to set up and use the project. Feel free to explore the different projects and experiment with different technologies to enhance your web development skills.