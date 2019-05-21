"""
Auth Views
"""
import logging

import jwt
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from chrty_backend import settings
from ..serializers import LoginSerializer, UserSerializer
from django.contrib.auth import login, logout, user_logged_in
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, status
from rest_framework_jwt.serializers import jwt_payload_handler


logger = logging.getLogger(__name__)


class RegisterView(generics.CreateAPIView):
    """
    Register View
    """
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        logging.info("Register new user:", serializer.data.get('email'))
        if user:
            return Response("Register successful!", status=201)


class LoginView(generics.CreateAPIView):
    """
    Login View
    """
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        if user is not None:
            login(request, user)
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                user_details['name'] = "%s %s" % (
                    user.first_name, user.last_name)
                user_details['token'] = token
                user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)
            except Exception as e:
                raise e
        logging.info(f'User {user.email} was logged in.')
        #         Token generation
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    """
    Logout View
    """
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        logout(request)
        return Response(status=204)
