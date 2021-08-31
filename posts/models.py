from django.db import models
from django.utils import timezone

from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название поста")
    text = models.TextField(verbose_name="Текст поста")
    image = models.ImageField(blank=True, null=True, verbose_name="Картинка поста")
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(verbose_name="URL", null=True, blank=True)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    