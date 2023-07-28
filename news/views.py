from django.shortcuts import render
from .services import get_article
from django.http import HttpResponse

def detail_views(request, pk):
    obj = get_article(pk)
    if obj is None:
        return HttpResponse('Not found(')
    else:
        context = {'obj':obj}
        return render(request, 'news/news_detail.html', context)
