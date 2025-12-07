Authentication System
---------------------
Files added:
- accounts/forms.py         (CustomUserCreationForm, ProfileForm)
- accounts/views.py         (register_view, profile_view)
- blog/urls.py              (login/logout/register/profile routes)
- blog/templates/blog/*     (login.html, register.html, profile.html, base.html)
- blog/static/blog/css/auth.css
- blog/static/blog/js/auth.js

Commands:
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

How to test:
1. Visit /register/ to create a new user (email required).
2. After registration, user is logged in and redirected to posts page.
3. Visit /login/ to authenticate; /logout/ to sign out.
4. Visit /profile/ to update first name, last name, email (POST handled).
