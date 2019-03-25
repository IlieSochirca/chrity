'''
RestApi endpoints
'''

from rest_api.views import views
from django.urls import include, path


urlpatterns = [
    path(r'posts', views.PostList.as_view())
]