import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from authentication.models import User
from common.token_auth import TokenAuth

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authorization_header = request.headers.get('Authorization')

        if not authorization_header:
            return None

        if len(authorization_header) < 2:
            raise AuthenticationFailed('Invalid Authentication')
        token = authorization_header.split(' ')[1]
        try:
            payload = TokenAuth.verify_token(token)
            user = User.objects.get(email=payload['email'])
            return (user, token)

        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            raise AuthenticationFailed('Invalid or expired token')
        
        