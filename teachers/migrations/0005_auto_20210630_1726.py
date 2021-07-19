# Generated by Django 3.1.3 on 2021-06-30 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_teacher_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['is_admin'], 'verbose_name': 'Учитель', 'verbose_name_plural': 'Учителя'},
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_admin',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(upload_to='teachers/', verbose_name='Фотография'),
        ),
    ]
