from .models import Article

def get_articles():
    """Getting all objects from the Article model"""
    queryset = Article.objects.all()
    return queryset

def get_article(pk):
    """Getting a specific object from the Article model"""
    queryset = Article.objects.get(id=pk)
    return queryset