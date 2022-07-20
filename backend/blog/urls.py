from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
]