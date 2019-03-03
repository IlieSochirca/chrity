'''
RestApi endpoints
'''



from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'posts', include('rest_api.posts.urls'))
]
