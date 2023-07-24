from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Name:')
    content = models.TextField(verbose_name='Content:')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Created at:')

    def __str__(self) -> str:
        return f'{self.title}'