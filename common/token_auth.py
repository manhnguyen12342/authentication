import datetime,jwt
from login.settings import SECRET_KEY
from authentication.models import User,BlacklistedToken
from rest_framework.exceptions import AuthenticationFailed

    
class TokenAuth():
    
      def create_token(User):
          
        user_token = {
            'email' :User.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(user_token, SECRET_KEY, algorithm='HS256')
        return token
    
      def verify_token(token):
          
        try:
            user_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            if BlacklistedToken.objects.filter(token=token).exists():
                raise AuthenticationFailed("Token has been blacklisted")
            return user_token
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token")
      
      def blacklist_token(token):
        try:
            BlacklistedToken.objects.create(token=token)
        except Exception as e:
            raise Exception("Failed to blacklist token:")
