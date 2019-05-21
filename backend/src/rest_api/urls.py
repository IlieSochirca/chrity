'''
RestApi endpoints
'''

from django.urls import path
from .views import PostList, PostDetail, LoginView, LogoutView, RegisterView

urlpatterns = []

posts_urls = [
    path(r'posts/', PostList.as_view(), name="posts-list"),
    path(r'posts/<int:pk>/', PostDetail.as_view(), name="posts-detail")
]

auth_urls = [
    path(r'auth/register/', RegisterView.as_view(), name="user-register"),
    path(r'auth/login/', LoginView.as_view(), name="user-login"),
    path(r'auth/logout/', LogoutView.as_view(), name="user-login"),

]

urlpatterns += auth_urls
urlpatterns += posts_urls
