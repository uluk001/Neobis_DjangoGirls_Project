from django.shortcuts import render, redirect
from .services import get_article
from .forms import ArticleForm
from django.http import HttpResponse

def detail_views(request, pk):
    obj = get_article(pk)
    if obj is None:
        return HttpResponse('Not found(')
    else:
        context = {'obj':obj}
        return render(request, 'news/news_detail.html', context)



def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ArticleForm()

    return render(request, 'news/create_article.html', {'form': form})