from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
    )
from django.core.validators import RegexValidator







class UserManager(BaseUserManager):
    """Manager for User"""
    def create_user(self, email, password=None, **extra_fields):
        """Create, save, and return a new user"""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        """Create new superuser."""
        user = self.create_user(email, password)
        user.is_doctor = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user






class User(AbstractBaseUser, PermissionsMixin):
    """The user model."""


    email = models.EmailField(max_length=100, unique=True, primary_key=True)
    government_id = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    address = models.CharField(max_length=250)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_doctor = models.BooleanField(default=False)
    password = models.CharField(max_length=100)
    is_superuser = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(validators = [RegexValidator(regex = r"^\+?1?\d{8,15}$")], max_length = 12, unique = True, default='+7')
    

    objects = UserManager()
    USERNAME_FIELD = 'email'
    
    
   