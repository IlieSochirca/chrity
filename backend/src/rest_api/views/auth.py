"""
Auth Views
"""
import logging

import jwt
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from ..serializers import LoginSerializer, UserSerializer
from django.contrib.auth import login, logout, user_logged_in
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, status


logger = logging.getLogger(__name__)
