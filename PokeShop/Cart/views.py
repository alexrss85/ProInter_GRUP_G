from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Carrito, ItemCarrito, User
from .serializers import CarritoSerializer, ItemCarritoSerializer, UpdateItemCarritoSerializer, UserSerializer

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

@api_view(['DELETE'])
def deleteCarrito(request, pk):
    carrito = Carrito.objects.filter(pk=pk).first()
    if not carrito:
        return Response({"error": "Carrito not found"}, status=status.HTTP_404_NOT_FOUND)
    
    carrito.delete()
    return Response({"message": "Carrito deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def createItemCarrito(request):
    serializer = ItemCarritoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listItemsCarrito(request):
    items = ItemCarrito.objects.all()
    serializer = ItemCarritoSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getItemCarrito(request, pk):
    item = ItemCarrito.objects.filter(pk=pk).first()
    if not item:
        return Response({"error": "ItemCarrito not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ItemCarritoSerializer(item)
    return Response(serializer.data)

@api_view(['PATCH'])
def updateItemCarrito(request, pk):
    item = ItemCarrito.objects.filter(pk=pk).first()
    if not item:
        return Response({"error": "ItemCarrito not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = UpdateItemCarritoSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteItemCarrito(request, pk):
    item = ItemCarrito.objects.filter(pk=pk).first()
    if not item:
        return Response({"error": "ItemCarrito not found"}, status=status.HTTP_404_NOT_FOUND)

    item.delete()
    return Response({"message": "ItemCarrito deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.filter(pk=pk).first()
    if not user:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateUser(request, pk):
    user = User.objects.filter(pk=pk).first()
    if not user:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.filter(pk=pk).first()
    if not user:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    user.delete()
    return Response({"message": "User deleted successfully"})