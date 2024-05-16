import uuid 
from django.db import models

from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    id_user = models.UUIDField(
        default = uuid.uuid4,
        unique = True,
        primary_key = True,
        editable = False
    )
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255 , unique = True)
    password = models.CharField(max_length=100)
    username = None
    
    USERNAME_FIELD = 'email'

