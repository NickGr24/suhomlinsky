# Generated by Django 3.1.3 on 2021-06-30 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_auto_20210531_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='URL'),
        ),
    ]