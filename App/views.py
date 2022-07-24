from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import status
from knox.auth import AuthToken
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Habitante, Departamento
from .serializers import RegisterSerializer, HabitanteSerializer, DepartamentoSerializer


@api_view(['POST'])
def Login_api(request):
    serializer = AuthTokenSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)
    user = serializer.validated_data['user']

    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info':{
            'id': user.id,
            'username': user.username,
            'email': user.email
            },
        'token': token
    }, status = status.HTTP_200_OK)


@api_view(['POST'])
def Register_api(request):
    serializer = RegisterSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)
    user = serializer.save()
    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info':{
            'id': user.id,
            'username': user.username,
            'email': user.email
            },
        'token': token
    }, status = status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def Lista_Habitantes(request, format = None):
    user = request.user
    if user.is_authenticated:
        if request.method == 'GET':
            habitantes = Habitante.objects.all()
            serializer = HabitanteSerializer(habitantes, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'POST':
            serializer = HabitanteSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)

            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    
    return Response({'Error':'Usuario no Autenticado'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'PUT', 'DELETE'])
def Solo_Habitante(request, cedula, format = None):
    user = request.user
    if user.is_authenticated:
        try:
            habitante = Habitante.objects.get(cedula = cedula)
        
        except Habitante.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = HabitanteSerializer(habitante)
            return Response(serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
            serializer = HabitanteSerializer(habitante, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)

            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            habitante.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
    
    return Response({'Error':'Usuario no Autenticado'}, status = status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'POST'])
def Lista_Departamentos(request, format = None):
    user = request.user
    if user.is_authenticated:
        if request.method == 'GET':
            departamento = Departamento.objects.all()
            serializer = DepartamentoSerializer(departamento, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)


        elif request.method == 'POST':
            serializer = DepartamentoSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    return Response({'Error':'Usuario no Autenticado'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'PUT', 'DELETE'])
def Solo_Departamento(request, id, format = None):
    user = request.user
    if user.is_authenticated:
        try:
            departamento = Departamento.objects.get(id = id)
        
        except Departamento.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = DepartamentoSerializer(departamento)
            return Response(serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
            serializer = DepartamentoSerializer(departamento, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)

            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            departamento.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
    
    return Response({'Error':'Usuario no Autenticado'}, status = status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def Departamento_Habitante(request, id = 0, format = None):
    user = request.user
    if user.is_authenticated:
        try:
            habitantes = Habitante.objects.filter(departamento_id = id)
       
        except Departamento.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = HabitanteSerializer(habitantes, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    return Response({'Error':'Usuario no Autenticado'}, status = status.HTTP_401_UNAUTHORIZED)
