from django.shortcuts import render
from . models import Article
from django.views.generic import ListView, DetailView
# Create your views here.
# The home page / view all posts.
class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'

# class for detailed view of articles on the blog.
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'