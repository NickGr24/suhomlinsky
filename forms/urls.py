from django.urls import path

from . import views

app_name = 'forms'

urlpatterns = [
    path('schedule/', views.schedule, name='schedule'),
    path('schedule/<int:id>/', views.detailedschedule, name='detailedschedule')
]