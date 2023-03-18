from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView, RetrieveAPIView,
                                     DestroyAPIView,
                                     RetrieveUpdateDestroyAPIView)
from django.contrib.auth.models import User
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUserOrStaffReadOnly, IsStaffOrReadOnly, IsAuthorOrReadOnly

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
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly )
    #lookup_field = 'slug'


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)


# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)
#
    # def delete(self, request):
    #     request.auth.delete()
    #     return Response(status=204)