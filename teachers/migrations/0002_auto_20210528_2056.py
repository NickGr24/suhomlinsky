# Generated by Django 3.1.3 on 2021-05-28 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='teachers/'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.CharField(blank=True, choices=[('русский язык и литература', 'Русский язык и Литература'), ('румынский', 'Румынский язык и литература'), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', '')], max_length=100, null=True),
        ),
    ]
