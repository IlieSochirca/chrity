from rest_framework import generics

from rest_api.posts import models
from rest_api.posts.serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer
