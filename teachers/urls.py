from django.urls import path

from . import views

urlpatterns = [
    path('teachers/', views.teacher_page, name='teachers')
]
