from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.posts_list, name='posts'),
    path('post/<str:slug>', views.post_detail, name='post_detail'),
]
