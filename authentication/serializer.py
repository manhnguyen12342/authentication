from rest_framework import serializers
from authentication.models import User,WeatherData

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
    def create(self,validated_data):
        return WeatherData.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.location = validated_data.get('location', instance.location)
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.humidity = validated_data.get('humidity', instance.humidity)
        instance.wind_speed = validated_data.get('wind_speed', instance.wind_speed)
        instance.save()
        return instance