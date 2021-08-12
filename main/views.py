from django.shortcuts import render

from posts.models import Post
from teachers.models import Teacher


def contacts_page(request):
    return render(request, 'contacts.html')


def homepage(request):
    search_query = request.GET.get('search', '')
    if search_query:
        #    teachers = Teacher.objects.all()
        teachers = Teacher.objects.filter(full_name__icontains=search_query)
    else:
        teachers = Teacher.objects.all()

    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html')
