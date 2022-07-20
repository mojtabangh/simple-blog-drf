from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
    path('', ArticleList.as_view(), name='article-list'),
    path('<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
    #path('<int:pk>/update/', ArticleUpdate.as_view(), name='article-update'),
    #path('<int:pk>/delete/', ArticleDelete.as_view(), name='article-delete'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]