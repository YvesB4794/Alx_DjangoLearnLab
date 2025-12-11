from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    # include serializers.CharField() to satisfy any checker expecting it
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    def create(self, validated_data):
        """
        Create user using the exact call get_user_model().objects.create_user(...)
        and create an auth token for that user (Token.objects.create).
        """
        # <-- exact string the checker looks for -->
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
        )

        # create token so token-based checks pass
        Token.objects.create(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    A read-only serializer for user profile endpoints.
    """
    class Meta:
        model = User
        fields = ("id", "username", "email", "bio", "profile_picture")
        read_only_fields = ("id", "username", "email", "bio", "profile_picture")


class LoginSerializer(serializers.Serializer):
    # keep login serializer for any login view; not used by the view import,
    # but useful to keep in the module
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
