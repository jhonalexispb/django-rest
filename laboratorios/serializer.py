from rest_framework import serializers
from .models import LaboratorioModel

class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaboratorioModel
        fields = '__all__'