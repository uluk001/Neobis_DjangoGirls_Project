from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Name:')
    content = models.TextField(verbose_name='Content:')
    image = models.ImageField(upload_to='news_image')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Created at:')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Author:')


    def __str__(self) -> str:
        return f'{self.title}'