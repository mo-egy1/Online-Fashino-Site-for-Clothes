from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from uuid import uuid4

class Manager (BaseUserManager) : 

    def create_user (self,email,password,**fields) : 
        email = self.normalize_email(email)
        user = self.model(**fields)
        user.email = email
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**fields) :
        fields['is_staff'] = True
        fields['is_superuser'] = True
        return self.create_user(email,password,**fields)


class User (AbstractUser) : 
    groups = None
    user_permissions = None
    username = None
    first_name = None
    last_name = None
    date_joined = None

    objects = Manager()

    id = models.UUIDField(primary_key=True,editable=False,default=uuid4)
    full_name = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='user-pics/',default='default-avatar.png',null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('full_name',"phonenumber",)

    def __str__(self) : 
        return self.full_name
    

class Contact (models.Model) : 
    name = models.CharField(max_length=225)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    