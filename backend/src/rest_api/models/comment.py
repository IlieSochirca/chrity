"""Comment Model Class"""
from django.db import models

from users.models import User
from .post import Post


class Comment(models.Model):
    """Comment Model"""
    name = models.CharField(max_length=150)
    content = models.CharField(max_length=450)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True)
    file = models.FileField(upload_to='documents', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
