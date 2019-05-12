"""
Auth Views
"""
from rest_framework.views import APIView
from ..serializers.auth import LoginSerializer, UserSerializer
from django.contrib.auth import login, logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication


class RegisterView(APIView):
    """
    Register View
    """

    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        print(serializer.initial_data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            return Response(serializer.data, status=201)


class LoginView(APIView):
    """
    Login View
    """

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
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
