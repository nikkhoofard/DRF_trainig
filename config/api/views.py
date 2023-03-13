from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView, RetrieveAPIView,
                                     DestroyAPIView,
                                     RetrieveUpdateDestroyAPIView)
from django.contrib.auth.models import User


from .serializer import ArticleSerializer, UserSerializer
# from ..blog.models import Article
from blog.models import Article


# Create your views here.
class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #lookup_field = 'slug'


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
