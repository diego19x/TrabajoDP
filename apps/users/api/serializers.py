"""
Serializers de usuarios para TIENDA - UrbanGear.
Maneja registro de nuevos compradores y visualización de perfil.
"""
from rest_framework import serializers
from apps.users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer para el registro de nuevos usuarios en UrbanGear."""

    class Meta:
        model        = User
        fields       = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email   =validated_data['email'],
            password=validated_data['password'],
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer de perfil público del usuario en UrbanGear."""

    class Meta:
        model  = User
        fields = ['id', 'username', 'email', 'phone', 'address']
