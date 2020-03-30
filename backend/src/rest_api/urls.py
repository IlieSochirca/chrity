'''
RestApi endpoints
'''

from django.urls import path
from rest_api import views
# from .views import PostList, PostDetail, LoginView, LogoutView, RegisterView, CommentsListCreateView

urlpatterns = []

posts_urls = [
    path(r'posts/', views.PostList.as_view(), name="posts-list"),
    path(r'posts/<int:pk>/', views.PostDetail.as_view(), name="posts-detail")
]

# auth_urls = [
#     path(r'auth/register/', views.RegisterView.as_view(), name="user-register"),
#     path(r'auth/login/', views.LoginView.as_view(), name="user-login"),
#     path(r'auth/logout/', views.LogoutView.as_view(), name="user-login"),
#
# ]

comments_urls = [
    path(r'posts/<int:pk>/comments/', views.CommentsListCreateView.as_view(), name="comments-list" )
]

# urlpatterns += auth_urls
urlpatterns += posts_urls
urlpatterns += comments_urls
