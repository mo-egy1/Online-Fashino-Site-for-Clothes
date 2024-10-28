from django.urls import path
from . import views

urlpatterns = [
    path('checkout/',views.checkout,name='checkout'),
    path('success/<str:payment_id>/',views.success,name='success'),
    path('cancel/<str:payment_id>/',views.cancel,name='cancel'),
]