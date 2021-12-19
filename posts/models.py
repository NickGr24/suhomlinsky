from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название поста", help_text="Название поста должно быть уникальным")
    text = models.TextField(verbose_name="Текст поста")
    image = models.ImageField(blank=True, null=True, verbose_name="Картинка поста")
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(verbose_name="URL", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        
class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'posts/')
    
    def __str__(self):
        return self.post.title
    
    class Meta:
        verbose_name = 'Картинка для поста'
        verbose_name_plural = 'Картинки для постов'