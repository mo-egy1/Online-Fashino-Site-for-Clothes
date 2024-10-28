from django.contrib import admin
from .models import Category, Model, Product#, Cart

@admin.register(Category)
class CategoryPanel (admin.ModelAdmin) :
    list_display = ('name',)

@admin.register(Model)
class ModelPanel (admin.ModelAdmin) :
    list_display = ('name',)

@admin.register(Product)
class PdPanel (admin.ModelAdmin) : 
    list_display = ('title','price',)

# @admin.register(Cart)
# class CartPanel (admin.ModelAdmin) : 
#     list_display = ('user','product','amount')
