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
    path('', views.PostListView.as_view(), name='post_list'),           # /posts/ as root
    path('posts/', views.PostListView.as_view(), name='posts_list'),    # optional alias
    path('posts/new/', views.PostCreateView.as_view(), name='post_new'), 
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    # ... other urls (auth etc) ...
]
