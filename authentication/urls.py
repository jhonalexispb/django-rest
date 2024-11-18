from django.urls import path
from .views import *

urlpatterns = [
    path('auth/login', LoginView.as_view(), name='login'),
]