
from django.contrib import admin
from django.urls import path, include

from dj_rest_auth.views import PasswordResetConfirmView

# from rest_framework.authtoken import views
# from api.views import RevokeToken

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/password/reset/confirm/<uid64>/<token>/',
         PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('api/rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),


    path('', include('blog.urls')),
    path('api/', include('api.urls')),


    # path("api/revoke/", RevokeToken.as_view()),
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/token-auth/', views.obtain_auth_token),


]
