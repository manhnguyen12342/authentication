import datetime,jwt
from django.shortcuts import render
from rest_framework.views import APIView
from login123.serializer import RegisterSerializer,LoginSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from login123.models import User
from django.contrib.auth.hashers import make_password
from token_auth import TokenAuth


class Registerview(APIView):
    def post(self,request):
          serializer = RegisterSerializer(data=request.data)
          serializer.is_valid(raise_exception=True)
          name = serializer.validated_data.get('name')
          email = serializer.validated_data.get('email')
          password = make_password(serializer.validated_data.get('password'))
          user = User.objects.create(name=name, email=email, password=password)
          return Response(serializer.data)
      
class LoginView(APIView):
    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        password = serializer.data['password']
        
        user = User.objects.filter(email = email).first()
        if not user.check_password(password) and user is None:
            raise AuthenticationFailed('Incorrect password or ! ')
        
        token = TokenAuth.create_token(user)
        
        return Response({
            'token':token,
            'user': serializer.data
            })
        
    
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.data = {
            'message': 'success'
        }
        return response