from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Facultades, Alumnos
from .serializers import FacultadesSerializer, AlumnosSerializer

# Vistas de la API

@api_view(['GET', 'POST'])
def facultadesApi(request):
    if request.method == 'GET':
        facultades = Facultades.objects.all()
        facultades_serializer = FacultadesSerializer(facultades, many=True)
        return JsonResponse(facultades_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        facultades_serializer = FacultadesSerializer(data=data)
        if facultades_serializer.is_valid():
            facultades_serializer.save()
            return JsonResponse("La facultad se agregó con éxito", safe=False)
        return JsonResponse("Error al guardar facultad", safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def facultadApi(request, id):
    try:
        facultad = Facultades.objects.get(FacultadId=id)
    except Facultades.DoesNotExist:
        return JsonResponse("La facultad no existe", status=404)

    if request.method == 'GET':
        facultades_serializer = FacultadesSerializer(facultad)
        return JsonResponse(facultades_serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        facultades_serializer = FacultadesSerializer(facultad, data=data)
        if facultades_serializer.is_valid():
            facultades_serializer.save()
            return JsonResponse("La facultad se actualizó con éxito", safe=False)
        return JsonResponse("Error al actualizar la facultad", safe=False)

    elif request.method == 'DELETE':
        facultad.delete()
        return JsonResponse("La facultad se eliminó con éxito", safe=False)

@api_view(['GET', 'POST'])
def alumnosApi(request):
    if request.method == 'GET':
        alumnos = Alumnos.objects.all()
        alumnos_serializer = AlumnosSerializer(alumnos, many=True)
        return JsonResponse(alumnos_serializer.data, safe=False)
    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            alumnos_serializer = AlumnosSerializer(data=data)
            if alumnos_serializer.is_valid():
                alumnos_serializer.save()
                return JsonResponse("Alumno agregado", safe=False)
            return JsonResponse("Error al guardar alumno", safe=False)
        except Exception as e:
            return JsonResponse(f"Error al guardar alumno: {str(e)}", safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def alumnoApi(request, id):
    try:
        alumno = Alumnos.objects.get(AlumnoId=id)
    except Alumnos.DoesNotExist:
        return JsonResponse("El alumno no existe", status=404)

    if request.method == 'GET':
        alumnos_serializer = AlumnosSerializer(alumno)
        return JsonResponse(alumnos_serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        alumnos_serializer = AlumnosSerializer(alumno, data=data)
        if alumnos_serializer.is_valid():
            alumnos_serializer.save()
            return JsonResponse("Alumno actualizado", safe=False)
        return JsonResponse("Error al actualizar el alumno", safe=False)

    elif request.method == 'DELETE':
        alumno.delete()
        return JsonResponse("Alumno eliminado", safe=False)

# Vistas para renderizar las plantillas HTML

def home(request):
    return render(request, 'index.html')

def mostrar_alumnos(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'index.html', {'alumnos': alumnos})
