from rest_framework import generics, permissions

from rest_api.models.post import Post
from rest_api.serializers.posts import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
