from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Categoria
from .serializers import CategoriaSerializer

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Catalog.models import Categoria, Product
from Catalog.serializers import CategoriaSerializer, ProductSerializer

@api_view(['GET'])
def getProductos(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createProducto(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def create_categoria(request):
    serializer = CategoriaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def list_categorias(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_categoria(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return Response(status=404)

    serializer = CategoriaSerializer(categoria, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_categoria(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk) 
        categoria.delete()
        return Response(status=204)  
    except Categoria.DoesNotExist:
        return Response({'detail': 'Categoria no encontrada.'}, status=404)