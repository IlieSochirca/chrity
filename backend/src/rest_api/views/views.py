from rest_framework import generics

from rest_api.models.post import Post
from rest_api.serializers.serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
