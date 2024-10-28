from django.shortcuts import render, redirect
from django.views import View
from product.models import Product
from user.models import Contact
from django.contrib import messages

class home_view (View) :
    def get(self,request,**kwargs) : 
        products = Product.objects.all()
        return render(request,'index.html',context={
            'products' : products,
            'arrival_pds' : products.order_by('?')
        })

class shop_view (View) :
    def get(self,request,**kwargs) : 
        products = Product.objects.all()
        return render(request,'shop.html',context={
            'products' : products,
        })

class about_view (View) :
    def get(self,request,**kwargs) : 
        return render(request,'about.html')

class blog_view (View) :
    def get(self,request,**kwargs) : 
        return render(request,'blog.html')

class contact_view (View) :
    def get(self,request,**kwargs) : 
        return render(request,'contact.html')


    def post(self,request,**kwargs) : 
        Contact.objects.create(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
        ).save()
        messages.success(request,'your data has been submitted !')
        return redirect('contact')
