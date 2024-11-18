from django.urls import path
from .views import *

urlpatterns = [
    path('list/', UserList.as_view(), name='user-list'),
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),
]