from django.db import models

DAYS_CHOICES = (
    ('Понедельник', 'Понедельник'),
    ('Вторник', 'Вторник'),
    ('Среда', 'Среда'),
    ('Четверг', 'Четверг'),
    ('Пятница', 'Пятница'),
)

class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название урока')
    cabinet = models.PositiveIntegerField(null=True, blank=True, verbose_name='Номер кабинета')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['cabinet']
        
    def __str__(self):
        return f"{self.name} {self.cabinet}"
    
class Form(models.Model):
    name = models.CharField(max_length=10, verbose_name="Класс")    
    
    def __str__(self):
       return self.name
    
    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

class Schedule(models.Model):
    klass = models.ForeignKey(Form, on_delete=models.DO_NOTHING, verbose_name='Класс')  
    week_day = models.CharField(max_length=50, choices=DAYS_CHOICES, verbose_name='День')
    first_subject = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, verbose_name='Первый урок', blank=True, null=True,related_name='first')
    second_subject = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, verbose_name='Второй урок',blank=True, null=True, related_name='second')
    third_subject = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, verbose_name='Третий урок',blank=True, null=True, related_name='third') 
    fourth_subject = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, verbose_name='Четвертый урок', blank=True, null=True,related_name='fourth')
    fifth_subject = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, verbose_name='Пятый урок', blank=True, null=True, related_name='fifth')
    sixth_subject = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, verbose_name='Шестой урок', blank=True, null=True, related_name='sixth')
    seventh_subject = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, verbose_name='Седьмой урок', blank=True, null=True, related_name='seventh')
    eigth_subject = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, verbose_name='Восьмой урок', blank=True, null=True, related_name='eigth')
    
    
    def __str__(self):
        return f"Расписание {self.klass} класса на {self.week_day}"

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"
    
class Pupil(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя ученика')
    form = models.ForeignKey(Form, on_delete=models.DO_NOTHING, verbose_name='Класс')
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
        