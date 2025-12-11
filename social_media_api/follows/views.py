from rest_framework import status, generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from posts.models import Post
from posts.serializers import PostSerializer
from .models import Follow
from .serializers import FollowSerializer

User = get_user_model()


class FollowUserView(generics.CreateAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_to_follow_id = kwargs["user_id"]
        user_to_follow = User.objects.get(id=user_to_follow_id)

        # prevent self-follow
        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself."},
                            status=status.HTTP_400_BAD_REQUEST)

        follow, created = Follow.objects.get_or_create(
            follower=request.user,
            following=user_to_follow
        )

        if not created:
            return Response({"detail": "Already following this user."},
                            status=status.HTTP_200_OK)

        return Response(FollowSerializer(follow).data, status=status.HTTP_201_CREATED)


class UnfollowUserView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user_to_unfollow = kwargs["user_id"]

        deleted, _ = Follow.objects.filter(
            follower=request.user,
            following_id=user_to_unfollow
        ).delete()

        if deleted == 0:
            return Response({"detail": "You are not following this user."},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "Unfollowed successfully."},
                        status=status.HTTP_200_OK)


class FollowersListView(generics.ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Follow.objects.filter(following_id=user_id)


class FollowingListView(generics.ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Follow.objects.filter(follower_id=user_id)


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_ids = Follow.objects.filter(
            follower=self.request.user
        ).values_list("following_id", flat=True)

        return Post.objects.filter(author_id__in=following_ids).order_by("-created_at")
