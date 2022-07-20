from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
)

from .models import Article
# Create your views here.
class ArticleListView(ListView):
    def get_queryset(self):
        return Article.objects.filter(status=True)


class ArticleDetailView(DetailView):
    def get_object(self):
        return get_object_or_404(
            Article.objects.filter(status=True),
            slug=self.kwargs.get('slug')
            )