from .models import Article

def get_articles():
    """Получаем все объекты с модели Article"""
    queryset = Article.objects.all()
    return queryset