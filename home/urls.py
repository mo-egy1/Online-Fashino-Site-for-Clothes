from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view.as_view(),name='home'),
    path('blog/',views.blog_view.as_view(),name='blog'),
    path('shop/',views.shop_view.as_view(),name='shop'),
    path('about/',views.about_view.as_view(),name='about'),
    path('contact/',views.contact_view.as_view(),name='contact'),
]