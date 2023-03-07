from django.urls import path, include
from .views import ArticleList

app_name = 'api'

urlpatterns = [
  path("v1", ArticleList.as_view(), name='list'),
]
