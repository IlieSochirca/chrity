'''
Post Model Serializer
'''

from rest_framework import serializers

from ..models.post import Post


class PostSerializer(serializers.ModelSerializer):
    """Post Serializer"""
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ("id", "title", "content", "created_at", "owner")
