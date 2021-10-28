from django.shortcuts import render
from posts.models import Post


def contacts_page(request):
    return render(request, 'contacts.html')

def schedule_page(request):
    return render(request, 'main/schedule.html')

def homepage(request):
    return render(request, 'home.html')
