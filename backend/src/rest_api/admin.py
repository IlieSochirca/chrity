# Register your models here.
from django.contrib import admin

from .models import post

models = [post.Post]
for model in models:
    admin.site.register(model)
