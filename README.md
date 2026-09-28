# Task Management System

A web-based Task Management System built using Django.

## Project Overview

This project is being developed to manage users and their tasks through a simple web-based application.

The project is currently under development. The initial version includes user authentication and a dashboard.

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Git
- GitHub

## Current Features

- User Login
- Django User Authentication
- Secure password authentication using Django
- User session management
- Dashboard
- CSRF protection

## Project Structure

```text
TaskManagement/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── users/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── templates/
│   ├── login.html
│   └── dashboard.html
│
├── static/
│   └── css/
│       └── login.css
│
├── db.sqlite3
├── manage.py
└── README.md
