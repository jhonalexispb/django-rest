from django.urls import path
from .views import *

urlpatterns = [
    path('list/', LaboratorioListView.as_view()),
    path('create/', LaboratorioCreateView.as_view()),
    path('update/<int:pk>/', LaboratorioUpdateView.as_view()),
    path('delete/<int:pk>/', LaboratorioDestroyView.as_view()),
]