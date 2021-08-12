from django.shortcuts import render, get_object_or_404

from posts.models import Post

from django.utils.translation import gettext_lazy as _

from .models import Teacher


def teacher_page(request):
    context = {
        'teachers': Teacher.objects.all()
    }
    return render(request, 'teachers/teachers.html', context)

def teacher_detail(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    return render(request, 'teachers/detail.html', {'teacher': teacher})
