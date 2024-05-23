from rest_framework import serializers
from authentication.models import User

class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=100)
    
    
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=100)
    

class UserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    user = LoginSerializer()

class WeatherDataSerializer(serializers.Serializer):
    date = serializers.DateField()
    location = serializers.CharField(max_length=100)
    temperature = serializers.FloatField()
    humidity = serializers.FloatField()
    wind_speed = serializers.FloatField()