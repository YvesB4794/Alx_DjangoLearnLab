# django-models Project

This project is a Django application demonstrating various types of relationships between models, including ForeignKey, ManyToMany, and OneToOne relationships.

## Project Structure

```
django-models
├── django_models
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── relationship_app
│   ├── migrations
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── tests.py
│   └── query_samples.py
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup Instructions

1. **Clone the Repository**: 
   If you haven't already, clone the repository containing the `Introduction_to_Django` project.

2. **Duplicate the Project Directory**: 
   Open your terminal and navigate to the directory containing the `Introduction_to_Django` project. Use the following command to duplicate the directory and rename it to `django-models`:
   ```
   cp -r Introduction_to_Django django-models
   ```

3. **Navigate to the New Project Directory**: 
   Change into the new project directory:
   ```
   cd django-models
   ```

4. **Create the relationship_app App**: 
   Run the following command to create a new app named `relationship_app`:
   ```
   python manage.py startapp relationship_app
   ```

5. **Define Models**: 
   In `relationship_app/models.py`, define the models for Author, Book, Library, and Librarian to demonstrate the relationships.

6. **Apply Database Migrations**: 
   Create and apply migrations to set up the database tables for the models:
   ```
   python manage.py makemigrations relationship_app
   python manage.py migrate
   ```

7. **Sample Queries**: 
   Implement sample queries in `relationship_app/query_samples.py` to interact with the models.

## Running the Project

To run the development server, use the following command:
```
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your web browser to see the application in action.