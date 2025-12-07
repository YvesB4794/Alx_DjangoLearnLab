Blog Post Management (CRUD)
---------------------------
Model: blog.models.Post

Views (class-based):
- PostListView (everyone)
- PostDetailView (everyone)
- PostCreateView (LoginRequired)
- PostUpdateView (LoginRequired + author only)
- PostDeleteView (LoginRequired + author only)

URLs:
- /posts/                (list)
- /posts/new/            (create, login required)
- /posts/<pk>/           (detail)
- /posts/<pk>/edit/      (edit, author only)
- /posts/<pk>/delete/    (delete, author only)

Forms:
- blog.forms.PostForm (fields: title, content). author set in view.

Commands:
- python manage.py makemigrations blog
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver
