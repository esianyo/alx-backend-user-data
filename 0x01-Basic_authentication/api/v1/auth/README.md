# Auth

This directory contains the authentication module for the API.

## Overview

The `auth` module provides classes and functions related to authentication within the API. It is responsible for managing user authentication, authorization headers, and current user information.

## Files

- `__init__.py`: This file is empty and serves as an indicator that the directory is a Python package.
- `auth.py`: This file contains the implementation of the `Auth` class, which handles authentication functionality within the API.

## Usage

To use the authentication module:

1. Import the `Auth` class from `auth.py`.
2. Create an instance of the `Auth` class.
3. Utilize the methods provided by the `Auth` class to manage authentication requirements, authorization headers, and current user information.

Example:

```python
from api.v1.auth.auth import Auth

# Create an instance of the Auth class
auth_manager = Auth()

# Check if authentication is required for a given path
require_auth = auth_manager.require_auth("/api/v1/status/", ["/api/v1/status/"])

# Get the authorization header
auth_header = auth_manager.authorization_header()

# Get the current user
current_user = auth_manager.current_user()

print(require_auth)
print(auth_header)
print(current_user)
```

## Methods

- `require_auth(path: str, excluded_paths: List[str]) -> bool`: Determines if authentication is required for a given path. Returns `True` if authentication is required, `False` otherwise.
- `authorization_header(request=None) -> str`: Retrieves the authorization header from the Flask request object. Returns `None` if the header is not found.
- `current_user(request=None) -> TypeVar('User')`: Retrieves information about the current user from the Flask request object. Returns `None` if no user is authenticated.

## Dependencies

The `auth` module has the following dependencies:

- Flask: A micro web framework for Python.
