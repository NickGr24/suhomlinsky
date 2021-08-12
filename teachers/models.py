from django.db import models

from django.urls import reverse 

SUBJECT_CHOICES = (
    ('русский язык и литература', 'Русский язык и Литература'),
    ('Румынский язык и литература', 'Румынский язык и литература'),
    ('Английский язык', 'Английский язык'),
    ('Украинский язык и литература', 'Украинский язык и литература'),
    ('История румын и всеобщая история', 'История румын и всеобщая история'),
    ('география', 'География'),
    ('биология', 'Биология'),
    ('информатика', ' Информатика'),
    ('химия', 'Химия'),
    ('физика', 'Физика'),
    ('математика', 'Математика'),
    ('Физическое воспитание', 'Физическое воспитание')
)

class Teacher(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES, verbose_name="Предмет")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='teachers/', verbose_name="Фотография")
    slug = models.SlugField(verbose_name="URL", null=True, blank=True)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("teacher_detail", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'