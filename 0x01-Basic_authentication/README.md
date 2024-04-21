# Basic Authentication

## Project Overview
This project focuses on implementing a Basic Authentication system for a simple API. You'll learn about authentication processes, Base64 encoding, and the mechanics of Basic authentication.

## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

## Tasks
### 0. Simple-basic-API
This task involves setting up a simple API with one model (User) and starting the server.

### 1. Error handler: Unauthorized
Implement an error handler for unauthorized requests with status code 401.

### 2. Error handler: Forbidden
Implement an error handler for requests where the user is authenticated but not allowed access, with status code 403.

### 3. Auth class
Create a class to manage API authentication, including methods for requiring authentication, extracting authorization headers, and identifying the current user.

### 4. Define which routes don't need authentication
Update the authentication class to define routes that don't require authentication.

### 5. Request validation!
Validate all requests to secure the API by checking for authentication headers and user authorization.

### 6. Basic auth
Create a BasicAuth class and update the API to use it for authentication based on the AUTH_TYPE environment variable.

### 7. Basic - Base64 part
Add a method to extract the Base64 part of the Authorization header for Basic Authentication.

### 8. Basic - Base64 decode
Add a method to decode the Base64 Authorization header for Basic Authentication.

### 9. Basic - User credentials
Add a method to extract user credentials from the decoded Base64 Authorization header for Basic Authentication.

### 10. Basic - User object
Add a method to create a User instance based on email and password for Basic Authentication.

### 11. Basic - Overload current_user
Overload the current_user method to retrieve the User instance for a request based on Basic Authentication.

## Copyright
© 2024 Esianyo Dzisenu. All rights reserved.
