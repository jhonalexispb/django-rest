from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from .models import LaboratorioModel
from .serializer import LaboratorioSerializer

class LaboratorioListView(generics.ListAPIView):
    queryset = LaboratorioModel.objects.all()
    serializer_class = LaboratorioSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        return Response({
            'message': 'Laboratorios fetched successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

class LaboratorioCreateView(generics.CreateAPIView):
    serializer_class = LaboratorioSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        return Response({
            'message': 'Laboratorio created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)
    
class LaboratorioUpdateView(generics.UpdateAPIView):
    queryset = LaboratorioModel.objects.all()
    serializer_class = LaboratorioSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)

            return Response({
                'message': 'Laboratorio updated successfully',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Laboratorios not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
class LaboratorioDestroyView(generics.DestroyAPIView):
    queryset = LaboratorioModel.objects.all()

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)

        return Response({
            'message': 'Laboratorio deleted successfully',
        }, status=status.HTTP_200_OK)