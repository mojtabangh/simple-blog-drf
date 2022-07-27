from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, ArticleViewSet

app_name = 'api'

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('articles', ArticleViewSet, basename='articles')

urlpatterns = [
    path('', include(router.urls)),
]