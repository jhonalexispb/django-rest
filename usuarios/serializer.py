from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Asegura que la contraseña no sea visible

    def create(self, validated_data):
        # Crea un nuevo usuario con una contraseña encriptada
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        # Si deseas permitir que un usuario actualice su contraseña
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)