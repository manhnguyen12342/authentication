import datetime,jwt
from django.shortcuts import render
from rest_framework.views import APIView
from login123.serializer import RegisterSerializer,LoginSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from login123.models import User


class registerviews(APIView):
    def post(self,request):
          serializer = RegisterSerializer(data=request.data)
          serializer.is_valid(raise_exception=True)
          name = serializer.validated_data['name']
          email = serializer.validated_data['email']
          password = serializer.validated_data['password']
          user = User.objects.create(name=name, email=email, password=password)
          return Response({"message": "User registered successfully"})
      
      
class LoginViews(APIView):
    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        password = serializer.data['password']
        
        user = User.objects.filter(email = email).first()
        
        if user is None:
            raise AuthenticationFailed('User not found !')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password ! ')
        payload = {
            'id': user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm ='HS256')
        
        response = Response()
        
        response.data ={
            'jwt':token
        }
        return response
    
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.data = {
            'message': 'success'
        }
        return response