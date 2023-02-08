from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

# Create your models here.

class Users(AbstractUser): 

    name = models.CharField(max_length=30)
    email= models.EmailField(max_length=90, unique=True)
    account_number = models.DecimalField(max_digits=6, decimal_places=0, unique=True)
    account_balance= models.DecimalField(max_digits=10, decimal_places=2, default= 0.00)

    object=CustomUserManager()
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= ['name', 'account_number']

    def __str__(self) -> str:
        return f'{self.account_number} {self.username}'


