'''
RestApi endpoints
'''

from django.urls import path
from rest_api.views import posts, auth

urlpatterns = []

posts_urls = [
    path(r'posts', posts.PostList.as_view(), name="posts-list")
]

auth_urls = [
    path(r'auth/register', auth.RegisterView.as_view(), name="user-register"),
    path(r'auth/login', auth.LoginView.as_view(), name="user-login"),
    path(r'auth/logout', auth.LogoutView.as_view(), name="user-login"),

]

urlpatterns += auth_urls
urlpatterns += posts_urls
