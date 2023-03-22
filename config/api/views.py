from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (ListCreateAPIView, RetrieveAPIView,
                                     DestroyAPIView,
                                     RetrieveUpdateDestroyAPIView)
from django.contrib.auth.models import User
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import (IsSuperUserOrStaffReadOnly,
                          IsStaffOrReadOnly,
                          IsAuthorOrReadOnly)

from .serializer import ArticleSerializer, UserSerializer
# from ..blog.models import Article
from blog.models import Article


# Create your views here.
# class ArticleList(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleDetail(DestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly )
#     #lookup_field = 'slug'

class ArticleViewsSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]

        return [permission() for permission in permission_classes]


# class UserList(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperUserOrStaffReadOnly,)


# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperUserOrStaffReadOnly,)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)

# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)
#
    # def delete(self, request):
    #     request.auth.delete()
    #     return Response(status=204)