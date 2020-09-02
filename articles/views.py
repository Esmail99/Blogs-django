from django.shortcuts import render
from .models import Article


def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles.html', {'articles': articles})


def article_details(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_details.html', {'article': article})
