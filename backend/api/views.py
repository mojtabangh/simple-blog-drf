from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAdminUser,
)
from django.contrib.auth.models import User

from api.serializers import ArticleSerializer, UserSerializer
from api.permissions import IsSuperUser, IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperUserOrStaffReadOnly
from blog.models import Article

# Create your views here.

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
        

class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


class ArticleUpdate(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDelete(RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)