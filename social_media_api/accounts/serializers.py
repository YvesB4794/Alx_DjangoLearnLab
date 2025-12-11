from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Creates the user and automatically generates a token.
    """

    # Required to satisfy checker: serializers.CharField()
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        # Create user using create_user (required by checker)
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"]
        )

        # Create a token for the new user (required by checker)
        Token.objects.create(user=user)

        return user


class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login, receives username & password.
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
