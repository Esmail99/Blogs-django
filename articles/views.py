from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms


def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles.html', {'articles': articles})


def article_details(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_details.html', {'article': article})


@login_required
def articles_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST)
        if form.is_valid():
            userToBeSaved = form.save(commit=False)
            userToBeSaved.author = request.user
            userToBeSaved.save()
            return redirect('home')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})
