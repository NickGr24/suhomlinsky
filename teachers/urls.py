from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('teachers/', views.teacher_page, name='teachers'),
    path('teachers/<slug:slug>/', views.teacher_detail, name='detail')

]
