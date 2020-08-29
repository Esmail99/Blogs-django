from django.http import HttpResponse
from django.shortcuts import render


def root(request):
    # return HttpResponse('<h1>Root URL</h1>')
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')
