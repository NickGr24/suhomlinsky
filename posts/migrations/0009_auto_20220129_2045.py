# Generated by Django 3.1.3 on 2022-01-29 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20211219_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название поста'),
        ),
    ]