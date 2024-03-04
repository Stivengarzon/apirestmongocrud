from django.urls import path
from Alumnos import views
from django.contrib import admin



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('api/facultades/', views.facultadesApi),
    path('api/facultades/<int:id>/', views.facultadApi, name='facultad-detail'),
    path('api/alumnos/', views.alumnosApi),
    path('api/alumnos/<int:id>/', views.alumnoApi),
    path('mostrar_alumnos/', views.mostrar_alumnos,name='alumno-detail'),
]