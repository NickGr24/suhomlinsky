# Generated by Django 3.1.3 on 2021-12-19 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_postimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postimage',
            options={'verbose_name': 'Картинка для поста', 'verbose_name_plural': 'Картинки для постов'},
        ),
    ]
