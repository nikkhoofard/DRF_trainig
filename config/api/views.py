# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView

from django.contrib.auth import get_user_model
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import (IsSuperUserOrStaffReadOnly,
                          IsStaffOrReadOnly,
                          IsAuthorOrReadOnly)

from .serializer import ArticleSerializer, UserSerializer, AuthorSerializer

from rest_framework import filters
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

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'author__username',
        'author__first_name',
        'title',
        'content',
                     ]
    ordering = ['-publish']
    ordering_fields = ['publish', 'updated', 'status']

    # def get_queryset(self):
    #     status = self.request.query_params.get('status')
    #     if status is not None:
    #         queryset = queryset.filter(status=status)
    #
    #     author = self.request.query_params.get('author')
    #     if author is not None:
    #         queryset = queryset.filter(author=author)
    #     return queryset

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
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)

# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)
#
    # def delete(self, request):
    #     request.auth.delete()
    #     return Response(status=204)

class AuthorRetrieve(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = (IsSuperUserOrStaffReadOnly,)