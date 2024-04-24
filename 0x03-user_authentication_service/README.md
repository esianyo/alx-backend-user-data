# User Authentication Service

This is a user authentication service implemented using Flask and SQLAlchemy.

## Requirements

- Python 3.7
- Flask
- SQLAlchemy
- bcrypt
- pycodestyle

## Setup

1. Install dependencies:

    ```bash
    pip3 install Flask SQLAlchemy bcrypt pycodestyle
    ```

2. Clone the repository:

    ```bash
    git clone https://github.com/esianyo/0x03-user_authentication_service.git
    ```

3. Navigate to the project directory:

    ```bash
    cd user-authentication-service
    ```

4. Run the Flask app:

    ```bash
    python3 app.py
    ```

## Usage

### Endpoints

- `POST /users`: Register a new user.
- `POST /sessions`: Log in and create a session.
- `DELETE /sessions`: Log out and destroy the session.
- `GET /profile`: View user profile.
- `POST /reset_password`: Get a reset password token.
- `PUT /reset_password`: Update password using the reset token.

### Example Usage

```bash
# Register a new user
curl -XPOST localhost:5000/users -d 'email=user@example.com' -d 'password=supersecret'

# Log in and create a session
curl -XPOST localhost:5000/sessions -d 'email=user@example.com' -d 'password=supersecret'

# View user profile
curl -XGET localhost:5000/profile -b "session_id=<session_id>"

# Log out and destroy the session
curl -XDELETE localhost:5000/sessions -b "session_id=<session_id>"

# Get a reset password token
curl -XPOST localhost:5000/reset_password -d 'email=user@example.com'

# Update password using the reset token
curl -XPUT localhost:5000/reset_password -d 'email=user@example.com' -d 'reset_token=<reset_token>' -d 'new_password=newsecret'
