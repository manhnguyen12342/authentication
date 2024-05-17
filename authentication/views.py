import datetime,jwt
from django.shortcuts import render
from rest_framework.views import APIView
from authentication.serializer import RegisterSerializer,LoginSerializer,UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from authentication.models import User
from django.contrib.auth.hashers import make_password
from common.token_auth import TokenAuth
from rest_framework_simplejwt.tokens import RefreshToken


class Registerview(APIView):
    def post(self,request):
          serializer = RegisterSerializer(data=request.data)
          serializer.is_valid(raise_exception=True)
          email = serializer.validated_data.get('email')
          if User.objects.filter(email=email).exists():
            return Response({'error': 'Email is already in use.'})
          name = serializer.validated_data.get('name')
          email = serializer.validated_data.get('email')
          raw_password = serializer.validated_data.get('password')
          encoded_password =make_password(raw_password)
          user = User.objects.create(name=name, email=email, password=encoded_password)
          user_serializer = RegisterSerializer(user)
          return Response(user_serializer.data)
      
class LoginView(APIView):
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
        authorization_header = request.headers.get('Authorization')
        if authorization_header:
            token = authorization_header.split()[-1]  # Tách chuỗi để lấy token
            try:
                # Đưa token vào danh sách đen
                RefreshToken(token).blacklist()
                return Response({'message': 'Logged out successfully'})
            except Exception as e:
                return Response({'error': 'Invalid token'})
        else:
            return Response({'error': 'Authorization header not provided'})
