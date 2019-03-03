'''
Post Model Endpoints

'''
from django.conf.urls import url

from rest_api.posts import views

urlpatterns = [
    url(r'', views.PostList.as_view()),
    # url(r'^<pk: int>', )
]
