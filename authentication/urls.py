from django.urls import path
""" from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
) """
from .views import *

urlpatterns = [
    #path('auth/login/', TokenObtainPairView.as_view()),
    #path('auth/refresh/', TokenRefreshView.as_view()),
    path('auth/login/', LoginView.as_view()),
]