from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.
class User(AbstractBaseUser):
    
    profile_image = models.TextField()
    nickname = models.CharField(max_length=24,unique=True)
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 254)
    
    USERNAME_FIELD = 'nickname'
    
    class Meta:
        db_table = "User"
    
        
class Follow(models.Model):
    
    following = models.ForeignKey('User',related_name='following', on_delete=models.CASCADE, default= '')
    user = models.ForeignKey('User', related_name='user',on_delete= models.CASCADE, default = '')
    class Meta:
        db_table = "Follow"
