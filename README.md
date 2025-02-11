### Project Structure

```
elearning-django/
├── config/                   # Main project folder
│   ├── __init__.py
│   ├── settings.py           # Settings for Django & DRF
│   ├── urls.py               # Main URL router
│   ├── wsgi.py
│   ├── asgi.py               # For Channels (WebSocket)
├── users/                    # User management
│   ├── migrations/           # Auto-generated migrations
│   ├── __init__.py
│   ├── models.py             # Custom user model
│   ├── serializers.py        # Serializers for user registration, login
│   ├── views.py              # Views for user registration, login
│   ├── urls.py               # URLs related to user
├── courses/                  # Course management
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py             # Course, Feedback models
│   ├── serializers.py        # Serializers for course and feedback
│   ├── views.py              # Views for creating courses, enrolling, feedback
│   ├── urls.py               # URLs for courses and feedback
├── chat/                     # Chat feature using WebSockets
│   ├── __init__.py
│   ├── consumers.py          # WebSocket consumers
│   ├── routing.py            # WebSocket routing
├── manage.py                 # Django management script
└── requirements.txt          # List of installed packages

```

## Features

- User registration, login, logout
- Course creation, enrollment, feedback
- Real-time chat using WebSockets
- REST API for user, course, feedback
- Custom user model
- Token-based authentication

## Technologies

- Django
- Django REST Framework
- Django Channels
- SQLite

## Installation

1. Clone the repository

```
git clone https://github.com/rejRoky/elearning-django.git

cd elearning-django
```

2. Create a virtual environment

```
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install the dependencies

```
pip install -r requirements.txt
```

4. Run the migrations

```
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser

```
python manage.py createsuperuser
```

6. Run the development server

```
python manage.py runserver
```

7. Open the browser and go to `http:// localhost:8000`
8. To access the admin panel, go to `http:// localhost:8000/admin` and login with the superuser credentials

## API Endpoints Swagger

- `http://localhost:8000/swagger/`
- `http://localhost:8000/redoc/`

## WebSocket Chat

- `ws://localhost:8000/ws/chat/`

