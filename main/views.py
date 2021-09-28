from django.shortcuts import render
from django.conf import settings
from posts.models import Post


def contacts_page(request):
    return render(request, 'contacts.html')

def schedule_page(request):
    return render(request, 'main/schedule.html')

def homepage(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html')
