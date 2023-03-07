from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .serializer import ArticleSerializer
# from ..blog.models import Article
from blog.models import Article


# Create your views here.
class ArticleList(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
