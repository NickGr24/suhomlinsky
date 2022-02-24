from django.contrib import admin

from .models import Form, Pupil, Schedule, Lesson

admin.site.register(Form)
admin.site.register(Pupil)
admin.site.register(Lesson)
admin.site.register(Schedule)
