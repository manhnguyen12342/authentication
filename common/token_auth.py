import datetime,jwt
from login.settings import SECRET_KEY
from authentication.models import User
from rest_framework_simplejwt.tokens import BlacklistedToken
    
class TokenAuth():
      def create_token(user):
        payload = {
            'email' :user.email ,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token
      def verify_token(token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            if BlacklistedToken.objects.filter(token=token).exists():
                raise jwt.InvalidTokenError("Token has been blacklisted")
            return payload
        except jwt.ExpiredSignatureError:
            raise jwt.ExpiredSignatureError("Token has expired")
        except jwt.InvalidTokenError:
            raise jwt.InvalidTokenError("Invalid token")
      def blacklist_token(token):
        try:
            BlacklistedToken.objects.create(token=token)
        except Exception as e:
            pass
