import datetime,jwt
from Login.settings import SECRET_KEY
from login123.models import User
    
class TokenAuth():
      def create_token(user):
        payload = {
            'id' :user ,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token
    
    