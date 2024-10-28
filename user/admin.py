from django.contrib import admin
from .models import User, Contact
from django.contrib.auth.models import Group

@admin.register(User)
class UserPanel (admin.ModelAdmin) : 
    list_display = ('full_name','email','phonenumber',)

@admin.register(Contact)
class ContactPanel (admin.ModelAdmin) : 
    list_display = ('name','email','subject',)



admin.site.unregister(Group)