from django.urls import path

from . import views

urlpatterns = [
    path('contacts/', views.contacts_page, name='contacts'),
    path('', views.homepage, name='homepage'),
    path('set_lang/', views.set_lang, name='set_lang'),
]
