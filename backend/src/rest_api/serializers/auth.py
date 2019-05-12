"""
Auth Serializers
"""
from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer
    """
    first_name = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    last_name = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField()

    # password2 = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data["email"], username=validated_data["username"],
                                        password=validated_data["password"],
                                        first_name=validated_data["first_name"], last_name=validated_data["last_name"])
        return user

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    raise exceptions.ValidationError("User is inactive!")

            else:
                raise exceptions.ValidationError("Unable to login with given credentials")
        else:
            raise exceptions.ValidationError("You must provide a valid username and password")
        return data
