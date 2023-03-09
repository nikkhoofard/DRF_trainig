from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .serializer import ArticleSerializer
# from ..blog.models import Article
from blog.models import Article


# Create your views here.
class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
