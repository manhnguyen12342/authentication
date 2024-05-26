from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from authentication.serializer import (
    RegisterSerializer,
    LoginSerializer,
    WeatherDataSerializer,
)
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from authentication.models import User, WeatherData
from django.contrib.auth.hashers import make_password
from common.token_auth import TokenAuth
from rest_framework.permissions import IsAuthenticated



class Registerview(APIView):
    authentication_classes=[]
    def post(self,request):
          serializer = RegisterSerializer(data=request.data)
          serializer.is_valid(raise_exception=True)
          email = serializer.validated_data.get('email')
          if User.objects.filter(email=email).exists():
            raise Exception({'error': 'Email is already in use.'})
          name = serializer.validated_data.get('name')
          email = serializer.validated_data.get('email')
          raw_password = serializer.validated_data.get('password')
          encoded_password =make_password(raw_password)
          user = User.objects.create(name=name, email=email, password=encoded_password)
          user_serializer = RegisterSerializer(user)
          return Response(user_serializer.data)

      
class LoginView(APIView):
    authentication_classes=[]
    
    def post(self,request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        user = User.objects.filter(email = email).first()
        if user is None or not user.check_password(password) :
            raise AuthenticationFailed('Incorrect password or email ! ')
        token = TokenAuth.create_token(user)
        return Response({
            'token':token
            })
        
        
class LogoutView(APIView):
    def post(self, request):
        token = request.auth
        TokenAuth.blacklist_token(token)
        return Response({'message': 'Logout successful'})
    

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
        return Response(serializer.data)


class WeatherDataDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        weather_data = WeatherData.objects.all()
        
        date = request.query_params.get('date', None)
        location = request.query_params.get('location', None)
        temperature = request.query_params.get('temperature', None)
        humidity = request.query_params.get('humidity', None)
        description = request.query_params.get('description', None)

        if date:
            weather_data = weather_data.filter(date=date)
        if location:
            weather_data = weather_data.filter(location__icontains=location)
        if temperature:
            weather_data = weather_data.filter(temperature=temperature)
        if humidity:
            weather_data = weather_data.filter(humidity=humidity)
        if description:
            weather_data = weather_data.filter(description__icontains=description)
        
        serializer = WeatherDataSerializer(weather_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class WeatherDataUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,id):
        Weather_id = WeatherData.objects.filter(id=id)
        serializer = WeatherDataSerializer(Weather_id, many=True)
        return Response(serializer.data)

    def put(self, request,id):
        weather_data = WeatherData.objects.get(id=id)
        serializer = WeatherDataSerializer(weather_data,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"complete update"})


class WeatherDataDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request,id):
        weather_data = WeatherData.objects.filter(id=id)
        weather_data.delete()
        return Response({"message":"Delete ok"})