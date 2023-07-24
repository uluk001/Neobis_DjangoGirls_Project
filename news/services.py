from .models import Article

def get_articles():
    queryset = Article.objects.all()
    return queryset