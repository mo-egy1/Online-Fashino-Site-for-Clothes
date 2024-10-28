from django.urls import path
from . import views

urlpatterns = [
    path('auth/logout/',views.logout_view.as_view(),name='logout'),
    path('auth/login/',views.login_view.as_view(),name='login'),
    path('auth/register/',views.register_view.as_view(),name='register'),
    path('profile/',views.profile_view,name='profile'),
]