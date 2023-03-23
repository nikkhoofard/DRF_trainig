from django.urls import path, include
# from .views import ArticleList, ArticleDetail, UserList, UserDetail
from .views import UserViewSet, ArticleViewsSet
from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()

router.register('users', UserViewSet, basename='articles')
router.register('articles', ArticleViewsSet, basename='users')


urlpatterns = [
  path("", include(router.urls))
  # path("", ArticleList.as_view(), name='list'),
  # path("<int:pk>", ArticleDetail.as_view(), name='DETAIL'),
  # path("users/", UserList.as_view(), name='user-list'),
  # path("users/<int:pk>", UserDetail.as_view(), name='user-detail'),

]
