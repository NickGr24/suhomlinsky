from django.shortcuts import render, get_object_or_404

from posts.models import Post

from django.utils.translation import gettext_lazy as _

from django.db.models import Q

from .models import Teacher


def teacher_page(request):
    teachers = Teacher.objects.all()    
    search_query = request.GET.get('search', '')

    if search_query and search_query != '':
        teachers = Teacher.objects.filter(Q(full_name__icontains=search_query)| 
        Q(description__icontains=search_query)|
        Q(subject__icontains=search_query)
        )
    else:
        teachers = Teacher.objects.all()

    context = {
        'teachers': teachers
    }
    return render(request, 'teachers/teachers.html', context)

def teacher_detail(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    return render(request, 'teachers/detail.html', {'teacher': teacher})
