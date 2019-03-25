'''
Post Model Serializer
'''

from rest_framework import serializers

from rest_api.models.post import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
