from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Carrito
from .serializers import CarritoSerializer

# Create your views here.

@api_view(['POST'])
def createCarrito(request):
    serializer = CarritoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listCarritos(request):
    carritos = Carrito.objects.all()
    serializer = CarritoSerializer(carritos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCarrito(request, pk):
    carrito = Carrito.objects.filter(pk=pk).first()
    if not carrito:
        return Response({"error": "Carrito not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CarritoSerializer(carrito)
    return Response(serializer.data)

@api_view(['PUT'])
def updateCarrito(request, pk):
    carrito = Carrito.objects.filter(pk=pk).first()
    if not carrito:
        return Response({"error": "Carrito not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CarritoSerializer(carrito, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteCarrito(request, pk):
    carrito = Carrito.objects.filter(pk=pk).first()
    if not carrito:
        return Response({"error": "Carrito not found"}, status=status.HTTP_404_NOT_FOUND)
    
    carrito.delete()
    return Response({"message": "Carrito deleted successfully"}, status=status.HTTP_204_NO_CONTENT)