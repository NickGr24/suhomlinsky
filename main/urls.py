from django.urls import path

from . import views

urlpatterns = [
    path('contacts/', views.contacts_page, name='contacts'),
    path('', views.homepage, name='homepage'),
    path('goleni/', views.goleni, name='goleni'),
    path('constantinovca/', views.constantinovca, name='constantinovca'),
    path('sofrincani/', views.sofrincani, name='sofrincani'),
]


