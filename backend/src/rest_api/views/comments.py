"""
Comments Views
"""
from rest_framework import generics

from ..models import Comment
from ..serializers import CommentSerializer


class CommentsListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
