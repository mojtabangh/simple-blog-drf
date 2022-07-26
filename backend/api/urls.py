from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, ArticleViewSet

app_name = 'api'

router = routers.SimpleRouter()
router.register('users', UserViewSet)
router.register('', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]