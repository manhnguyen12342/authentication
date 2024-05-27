from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from CRUD.serializer import WeatherDataSerializer
from CRUD.models import WeatherData
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class WeatherDataListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        weather_data = WeatherData.objects.all()
        serializer =WeatherDataSerializer(weather_data, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = WeatherDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("update complete", serializer.data,status=status.HTTP_201_CREATED)


class WeatherDataDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        weather_data = WeatherData.objects.all()
        serializer = WeatherDataSerializer(weather_data)
        return Response(serializer.data)
    

class WeatherDataUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        
        weather_data = WeatherData.objects.filter(id=id).first
        if  weather_data is None :
            return Response({"message": "InValid ID"})
        serializer = WeatherDataSerializer(weather_data)
        return Response(serializer.data)


    def put(self, request, id):
        weather_data = WeatherData.objects.filter(id=id)
        if not weather_data :
            return Response({"message":"Invalid ID"},status=status.HTTP_404_NOT_FOUND)
        serializer = WeatherDataSerializer(weather_data, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Update completed"})


class WeatherDataDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        
        weather_data = WeatherData.objects.filter(id=id).first
        if  weather_data is None :
            return Response({"message": "InValid ID"})
        serializer = WeatherDataSerializer(weather_data)
        return Response(serializer.data)

    
    def delete(self, request,id):
        
        weather_data = WeatherData.objects.filter(id=id)
        if not weather_data :
            return Response({"message":"Invalid ID"},status=status.HTTP_404_NOT_FOUND)
        weather_data.delete()
        return Response({"message":"Delete ok"},status=status.HTTP_204_NO_CONTENT)
