from django.shortcuts import render

from posts.models import Post

from .models import Teacher

def homepage(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'teachers/home.html')

def teacher_page(request):
    context = {
        'teachers': Teacher.objects.all()
    }
    return render(request, 'teachers/teachers.html', context)