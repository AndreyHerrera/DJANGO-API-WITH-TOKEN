from django.contrib.auth.models import User
from rest_framework import serializers, validators
from .models import Habitante, Departamento


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()      

        return user


class HabitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitante
        fields = ['id', 'cedula', 'nombres', 'apellidos', 'direccion', 'telefono', 'ciudad', 'departamento']


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ['id', 'departamento']