# Zoo and Users Management

This project is a simple web application for managing users and zoo entities. It uses Flask for the backend, SQLAlchemy for database interaction, and Axios for handling asynchronous requests in the front end.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features
- Add, update, and delete users
- Add, update, and delete zoo entities
- View a list of users and zoo entities

## Technologies Used
- Flask
- SQLAlchemy
- Axios
- Bootstrap
- SQLite (as the default database)

## Getting Started
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/zoo-and-users-management.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:
    ```bash
    python app.py
    ```

4. Open your browser and go to [http://localhost:5000](http://localhost:5000)

## Usage
- Add new users and zoo entities through the provided forms.
- Update existing users and zoo entities by clicking the "Update" button.
- Delete users and zoo entities by clicking the "Delete" button.

## Endpoints
- **GET /users**: Get a list of all users.
- **GET /users/{user_id}**: Get details of a specific user.
- **POST /users**: Add a new user.
- **PUT /users/{user_id}**: Update an existing user.
- **DELETE /users/{user_id}**: Delete a user.

- **GET /zoo**: Get a list of all zoo entities.
- **GET /zoo/{entity_id}**: Get details of a specific zoo entity.
- **POST /zoo**: Add a new zoo entity.
- **PUT /zoo/{entity_id}**: Update an existing zoo entity.
- **DELETE /zoo/{entity_id}**: Delete a zoo entity.

## Contributing
1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
