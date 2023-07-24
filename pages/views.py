from django.shortcuts import render
from news.services import get_articles

def main(request):
    articles = get_articles()
    context = {'articles':articles}
    return render(request, 'index.html', context)