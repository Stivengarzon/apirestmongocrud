from django.shortcuts import render
from django.http import JsonResponse
from .models import Cliente
import json

def api_clientes(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all().values()
        return JsonResponse(list(clientes), safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        cliente = Cliente.objects.create(
            nombre=data['nombre'],
            apellido=data['apellido'],
            email=data['email'],
            edad=data['edad']
        )
        return JsonResponse({'mensaje': 'Cliente creado correctamente'}, status=201)

def index(request):
    # Obtener los datos de los clientes desde la API de clientes
    response = api_clientes(request)
    clientes_data = json.loads(response.content)

    # Convertir los datos en objetos Cliente
    clientes = [Cliente(**cliente_data) for cliente_data in clientes_data]

    # Pasar los objetos Cliente a la plantilla
    return render(request, 'index.html', {'clientes': clientes})
