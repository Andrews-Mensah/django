from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def drink_list(request):

    #get all the drinks:
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse({"Drinks":serializer.data});


    #create drinks
    elif request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id):

    try:
        drinkId = Drink.objects.get(pk=id);
    except Drink.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drinkId)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drinkId, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE':
        # serializer = DrinkSerializer(drinkId)
        # if serializer.is_valid():
            drinkId.delete()
            return Response({"message":'Drink deleted', "status": status.HTTP_204_NO_CONTENT})
            
