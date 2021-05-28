from django.db import models

SUBJECT_CHOICES = (
    ('русский язык и литература', 'Русский язык и Литература'),
    ('румынский', 'Румынский язык и литература'),
    ('английский', 'Английский язык'),
    ('украинский', 'Украинский язык и литература'),
    ('история', 'История румын и всеобщая история'),
    ('география', 'География'),
    ('биология', 'Биология'),
    ('информатика', 'информатика'),
    ('химия', 'Химия'),
    ('физика', 'Физика'),
    ('математика', 'Математика'),
    ('физкультура', 'Физическое воспитание')
)

class Teacher(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES, blank=True, null=True, verbose_name="Предмет")
    description = models.TextField(null=True, blank=True,  verbose_name="Описание")
    image = models.ImageField(upload_to='teachers/', null=True, blank=True, verbose_name="Фотография")


    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['full_name']
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'