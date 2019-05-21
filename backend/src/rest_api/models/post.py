from django.db import models

from users.models import User


class Post(models.Model):
    """Post Model"""
    title = models.CharField(max_length=120)
    content = models.TextField()
    file = models.FileField(upload_to='documents', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    like = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
