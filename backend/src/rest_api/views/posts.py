from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404

from ..models import Post
from ..serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """List and Create Api view"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """Post Detail View"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
