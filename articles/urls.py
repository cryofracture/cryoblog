from django.urls import path
from . import views
import random

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='detail') # this path opens a unique URL for the detailed view into the article. 
]