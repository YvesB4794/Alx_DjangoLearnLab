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


Comment system
--------------
Model: blog.models.Comment
- post: FK -> Post (related_name='comments')
- author: FK -> User
- content: TextField
- created_at: auto_now_add
- updated_at: auto_now

Forms:
- blog.forms.CommentForm for create/edit
  - content validated to be non-empty and <=2000 chars

Views & URLs:
- POST new comment (inline): POST to /post/<post_pk>/comment/new/ (login required)
- Edit comment: /comment/<pk>/edit/ (only author)
- Delete comment: /comment/<pk>/delete/ (only author)

Templates:
- Inline comments and create form are integrated into blog/templates/blog/post_detail.html
- Edit and delete use blog/templates/blog/comment_form.html and comment_confirm_delete.html

Testing:
- Anonymous users can view comments.
- Only authenticated users can post.
- Only comment authors can edit or delete their own comments.


Tagging & Search
----------------
- Model: Tag (name)
- Post.tags: ManyToManyField to Tag
- Add tags when creating/editing posts (comma separated)
- Click a tag name to see posts with that tag: /tag/<tag_name>/
- Search across title, content and tags via header search: /search/?q=keyword
