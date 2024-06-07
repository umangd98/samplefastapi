

# FastAPI Web Application Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Project Structure](#project-structure)
5. [Database Configuration](#database-configuration)
6. [Running the Application](#running-the-application)
7. [Endpoints](#endpoints)
    - [Signup](#signup)
    - [Login](#login)
    - [AddPost](#addpost)
    - [GetPosts](#getposts)
    - [DeletePost](#deletepost)
8. [Authentication](#authentication)
9. [Database Migrations](#database-migrations)
10. [Caching](#caching)
11. [Dependencies](#dependencies)

## Introduction

This documentation provides a comprehensive guide to a web application built with FastAPI, SQLAlchemy, and Pydantic, following the MVC design pattern. The application includes user authentication and CRUD operations for posts, utilizing token-based authentication and caching mechanisms.

## Requirements

- Python 3.8+
- MySQL
- pip

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/umangd98/samplefastapi.git
    cd yourrepository
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Project Structure

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   ├── auth.py
│   └── routes
│       ├── __init__.py
│       ├── auth.py
│       └── post.py
├── alembic
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── 2024XXXX_XXXX_create_tables.py
├── alembic.ini
└── requirements.txt
```

## Database Configuration

1. Create a MySQL database for the application.

2. Update the `SQLALCHEMY_DATABASE_URL` in `app/database.py` with your MySQL database configuration:
    ```python
    SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user:password@localhost/dbname"
    ```

## Running the Application

To run the FastAPI application, use the following command:
```bash
uvicorn app.main:app --reload
```

## Endpoints

### Signup
- **URL:** `/auth/signup`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "email": "user@example.com",
        "password": "password123"
    }
    ```
- **Response:**
    ```json
    {
        "id": 1,
        "email": "user@example.com"
    }
    ```

### Login
- **URL:** `/auth/login`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "username": "user@example.com",
        "password": "password123"
    }
    ```
- **Response:**
    ```json
    {
        "access_token": "jwt_token",
        "token_type": "bearer"
    }
    ```

### AddPost
- **URL:** `/post/addpost`
- **Method:** `POST`
- **Headers:**
    ```json
    {
        "Authorization": "Bearer jwt_token"
    }
    ```
- **Request Body:**
    ```json
    {
        "text": "This is a new post"
    }
    ```
- **Response:**
    ```json
    {
        "id": 1,
        "text": "This is a new post",
        "owner_id": 1
    }
    ```

### GetPosts
- **URL:** `/post/getposts`
- **Method:** `GET`
- **Headers:**
    ```json
    {
        "Authorization": "Bearer jwt_token"
    }
    ```
- **Response:**
    ```json
    [
        {
            "id": 1,
            "text": "This is a new post",
            "owner_id": 1
        }
    ]
    ```

### DeletePost
- **URL:** `/post/deletepost/{post_id}`
- **Method:** `DELETE`
- **Headers:**
    ```json
    {
        "Authorization": "Bearer jwt_token"
    }
    ```
- **Response:**
    ```json
    {
        "message": "Post deleted successfully"
    }
    ```

## Authentication

The application uses token-based authentication. Tokens are generated upon successful login and must be included in the `Authorization` header for endpoints that require authentication.

## Database Migrations

Alembic is used for database migrations. 

1. Initialize Alembic:
    ```bash
    alembic init alembic
    ```

2. Create a new migration:
    ```bash
    alembic revision --autogenerate -m "create tables"
    ```

3. Apply the migrations:
    ```bash
    alembic upgrade head
    ```

## Caching

In-memory caching is implemented for the `get_posts` endpoint using `cachetools`. Cached data is stored for up to 5 minutes.

## Dependencies

- `fastapi`
- `uvicorn`
- `sqlalchemy`
- `pydantic`
- `jose`
- `passlib`
- `cachetools`
- `mysqlclient`

## License

This project is licensed under the MIT License.

---

This documentation provides an overview of the application structure, installation steps, endpoint details, and other relevant information to help you understand and use the application.