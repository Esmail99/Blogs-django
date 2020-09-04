from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles_list, name='list'),
    path('create/', views.articles_create, name='create'),
    path('<slug:slug>/', views.article_details, name='details'),
]
