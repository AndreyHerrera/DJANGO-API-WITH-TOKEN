from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from knox import views as knox_views
from . import views

urlpatterns = [
    path('login/', views.Login_api, name = 'Login'),
    path('register/', views.Register_api, name = 'Registro'),
    path('logout/', knox_views.LogoutView.as_view(), name = 'Logout'),
    path('habitante/', views.Lista_Habitantes, name='Lista de Habitantes'),
    path('habitante/<int:cedula>/', views.Solo_Habitante, name='Habitante'),
    path('departamento/', views.Lista_Departamentos, name='Lista de Departamentos'),
    path('departamento/<int:id>/', views.Solo_Departamento, name='Departamento'),
    path('departamento_habitantes/<int:id>/', views.Departamento_Habitante, name='Departamento Habitantes'),
]

urlpatterns = format_suffix_patterns(urlpatterns)