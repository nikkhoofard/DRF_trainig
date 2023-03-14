from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView, RetrieveAPIView,
                                     DestroyAPIView,
                                     RetrieveUpdateDestroyAPIView)
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from .permissions import IsSuperUser, IsStaffOrReadOnly, IsAuthorOrReadOnly

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
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)
    #lookup_field = 'slug'


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)