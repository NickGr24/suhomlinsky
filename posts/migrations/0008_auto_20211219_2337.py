# Generated by Django 3.1.3 on 2021-12-19 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20211219_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='Название поста должно быть уникальным', max_length=255, verbose_name='Название поста'),
        ),
    ]
