from django.shortcuts import render
from rest_framework.views import APIView
from authentication.serializer import (
    RegisterSerializer,
    LoginSerializer,
)
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from authentication.models import User
from django.contrib.auth.hashers import make_password
from common.token_auth import TokenAuth


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
    

