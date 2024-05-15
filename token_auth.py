import datetime,jwt
from rest_framework.response import Response

def create_token(user):
    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }
    
    # Encode the payload to create the JWT token
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    
    # Prepare the response with the JWT token
    response = Response()
    response.data = {
        'jwt': token
    }
    
    return response