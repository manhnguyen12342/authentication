import datetime,jwt
from login.settings import SECRET_KEY
from authentication.models import User
from rest_framework_simplejwt.tokens import RefreshToken
    
class TokenAuth():
      def create_token(user):
        payload = {
            'email' :user.email ,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token
      
class RefreshToken:
    def blacklist_token(token):
        # In a real-world scenario, you might want to store blacklisted tokens in a database
        # Here, I'm just storing them in memory for simplicity
        if 'blacklisted_tokens' not in globals():
            globals()['blacklisted_tokens'] = set()
        globals()['blacklisted_tokens'].add(token)

    @staticmethod
    def is_token_blacklisted(token):
        return token in globals().get('blacklisted_tokens', set())
    
    