from rest_framework import serializers
from login123.models import User

class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=100)
    
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=100)
