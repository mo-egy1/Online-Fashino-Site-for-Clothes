from django.shortcuts import render, redirect
from django.views import View
from user.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def profile_view (request):
    user = request.user
    if request.method == "POST" : 
        user.full_name = request.POST.get('full_name')
        user.email = request.POST.get('email')
        user.phonenumber = request.POST.get('phonenumber')

        if 'picture' in request.FILES : 
            user.picture = request.FILES.get('picture')
        user.save()
        messages.success(request,'profile has been updated')
        
        return redirect('profile')
    
    return render(request,'profile.html')

class logout_view (View) : 
    def get(self,request,**kwargs) : 
        res = redirect('home')
        res.delete_cookie('sessionid')
        return res
    


class login_view (View) : 
    def get(self,request,**kwargs) :
        return render(request,'login.html')

    def post(self,request,**kwargs) : 
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)

        try :
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request,'invalid email')
            return redirect('login')
        
        if not user.check_password(password) : 
            messages.error(request,'invalid password')
            return redirect('login')
        
        login(request,user)
        return redirect('home')


class register_view (View) : 
    def get(self,request,**kwargs) : 
        return render(request,'signup.html')
    
    def post (self,request,**kwargs) : 
        req_arr = {**request.POST}
        data = {}

        for key,val in req_arr.items() : 
            data[key] = val[0]

        if User.objects.filter(email=data['email']).count() != 0 : 
            messages.error(request,'this email already taken by another user.')
            return redirect('register')


        data['phonenumber'] = f'+2{data["phonenumber"]}'

        data.pop('csrfmiddlewaretoken')
        
        user = User.objects.create_user(**data)
        if 'picture' in request.FILES : 
            user.picture = request.FILES.get('picture')
        user.save()
        
        login(request,user)
        return redirect('home')
    

    