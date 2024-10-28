from django.shortcuts import render, redirect
from .models import Product
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import Cart
from django.contrib import messages

class get_product (View) : 
    
    def get(self,request,product_id,**kwargs) : 
        
        try : 
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return redirect('home')
        
        return render(request,'product.html',{
            'product' : product
        })
    


@login_required
def cart (request) :
    if 'del' in request.GET :
        try :
            Cart.objects.get(id=request.GET.get('del')).delete()
        except Cart.DoesNotExist:
            pass
        return redirect('cart')

    cart = Cart.objects.filter(user=request.user)

    return render(request,'cart.html',{
        'cart_products' : cart,
        'cart_total' : Cart.get_total_price(request.user)
    })


@login_required
def add_to_cart(request,product_id) : 
    if request.method == "POST" : 
        try :
            cart = Cart.objects.create(
                user = request.user,
                product = Product.objects.get(id=product_id),
                amount=request.POST.get('amount',1)
            )
            cart.save()
            messages.success(request,'the product has been added to cart successfully !')
        except Exception as error:
            print('the error in cart : ', error)
            messages.error(request,'error accoured when add the product to the cart ')
        return redirect('product',product_id)
