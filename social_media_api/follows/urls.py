from django.urls import path
from .views import (
    FollowUserView,
    UnfollowUserView,
    FollowersListView,
    FollowingListView,
    FeedView
)

urlpatterns = [
    path('', FollowUserView.as_view(), name='follow-user'),  # POST /api/follows/
    path('unfollow/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('followers/<int:user_id>/', FollowersListView.as_view(), name='followers'),
    path('following/<int:user_id>/', FollowingListView.as_view(), name='following'),
]
