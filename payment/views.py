from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import stripe
from payment.models import Payment
from product.models import Cart
from Project import settings
from django.contrib import messages


stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request) :
    user = request.user
    amount = Cart.get_total_price(user)
    redirect_to = "http://127.0.0.1:8000/payment"
    payment = Payment.objects.create(
        user=user,
        price=amount,
    )
    payment.save()
    session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(amount) * 100, 
                    'product_data': {
                        'name': 'Payment',
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            # here you should return to the frontend server no backend
            success_url=f'{redirect_to}/success/{payment.id}/',
            cancel_url=f'{redirect_to}/cancel/{payment.id}/',
            customer_email=user.email
        )
    return redirect(session.url)

@login_required
def success (request,payment_id):
    try : 
        payment = Payment.objects.get(id=payment_id)
    except Payment.DoesNotExist:
        messages.error(request,'invalid payment id')
        return redirect('cart')
    
    if payment.user != request.user : 
        messages.error(request,'invalid payment id')
        return redirect('cart')
    
    payment.state = 'success'
    payment.save()

    Cart.objects.filter(user=request.user).delete()
    return render(request,'payment-success.html')

@login_required
def cancel (request,payment_id):
    try : 
        payment = Payment.objects.get(id=payment_id)
    except Payment.DoesNotExist:
        messages.error(request,'invalid payment id')
        return redirect('cart')
    
    if payment.user != request.user : 
        messages.error(request,'invalid payment id')
        return redirect('cart')
    
    payment.state = 'cancel'
    payment.save()

    return render(request,'payment-cancel.html')
