'''
Post Model Serializer
'''

from rest_framework import serializers

from rest_api.models.post import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ("id", "title", "content", "created_at", "owner")
