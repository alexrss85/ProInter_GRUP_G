from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Categoria, Product
from .serializers import CategoriaSerializer, ProductSerializer
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def getProductos(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProducto(request, pk):
    product = Product.objects.filter(pk=pk).first()
    if not product:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['POST'])
def createProducto(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateProducto(request, pk):
    product = Product.objects.filter(pk=pk).first()
    if not product:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteProducto(request, pk):
    product = Product.objects.filter(pk=pk).first()
    if not product:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
    product.delete()
    return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

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
    categoria = Categoria.objects.filter(pk=pk).first()
    
    if not categoria:
        return Response({"error": "Categoria no encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    categoria.delete()
    return Response({"message": "Categoria eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)