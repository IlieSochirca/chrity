# Register your models here.
from django.contrib import admin

from .models import post, comment

models = [post.Post, comment.Comment]
for model in models:
    admin.site.register(model)
