from django.urls import path
from . import views
from .views import register_view, profile_view
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views

app_name = 'blog'

urlpatterns = [
    # existing blog urls...
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # Authentication
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    #path("register/", register_view, name="register"),
    #path("profile/", profile_view, name="profile"),
    path('register/', accounts_views.register_view, name='register'),
    path('profile/', accounts_views.profile_view, name='profile'),
     # LIST & DETAIL
    path('', views.PostListView.as_view(), name='post_list'),  
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    # CREATE
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    # UPDATE
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    # DELETE
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    # Comments
    path('post/<int:post_pk>/comment/new/', views.comment_create_view, name='comment_new'),
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('post/<int:pk>/comment/new/', views.CommentCreateView.as_view(), name='comment_create'),

]
