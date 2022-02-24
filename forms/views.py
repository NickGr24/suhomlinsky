from django.shortcuts import render, redirect

from .models import Lesson, Form, Schedule, Pupil

from django.shortcuts import get_object_or_404


def detailedschedule(request, id):
    id = request.GET.get('klass')
    print(id)
    klass = Schedule.objects.get(id=id)
    context = {
    'classes': Form.objects.all(),
    'klass_schedule': klass
    }
    return render(request, 'forms/detailed-schedule.html', context)

def schedule(request):
    schedule_id = request.GET.get('klass')
    print(schedule_id)
    context = {
    'classes': Form.objects.all(),
    }
    return render(request, 'forms/schedule.html', context)
