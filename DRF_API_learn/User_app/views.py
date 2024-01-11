from django.shortcuts import render
from django.contrib.auth.models import User
from User_app.forms import Create_user_form,Login_form
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rest_framework.authtoken.models import Token
#from django.shortcuts import redirect

# Create your views here.

#home 
def index(request):
    return render(request,'User_app/index.html')


#create_user
def create_user(request):
    Flag=False
    message=''
    user_form=Create_user_form()
    
    if(request.method=="POST"):
        
        user_form=Create_user_form(data=request.POST)
        if(user_form.is_valid()):
            
            #save user credentials           
            
            """first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            email=request.POST.get('email')
            username=request.POST.get('username')
            password=request.POST.get('password')"""
            
            
            
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            Flag=True

            message="Succcesfully Created User profile"         
            return render(request,'User_app/createusersuccess.html',{'username':request.POST['username']})     
        else:
            message="User profile not Created"
    else:
        message=''
    return render(request,'User_app/create_user.html',{"form":user_form})  

    
def user_login(request):
    authenticated=False
    if(request.method=="POST"):

        login_form=Login_form(request.POST)

        if(login_form.is_valid()):

            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            #user=authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
            user=authenticate(request,username=username,password=password)

            if user is not None:
                
        
                username = login_form.cleaned_data['username']
                user_instance=User.objects.get(username=username)
                token=Token.objects.get(user=user_instance)
                
                login(request, user)
                return render(request, 'User_app/api_token_page.html', {'username': request.POST.get('username'),'token':token})

                authenticated=True
            else:
                # Authentication failed
                return render(request, 'User_app/User_login.html', {'form': login_form})

        login_form=Login_form()
    else:
        login_form=Login_form()                

    return render(request,'User_app/User_login.html',{"form":login_form,})

@login_required
def token_view(request):
    username=request.user
    user_instance=User.objects.get(username=username)
    try:
        token=Token.objects.get(user=user_instance)

    except:
        token='NONE'

    return(render(request,'User_app/api_token_page.html',{'username':username,'token':token}))

@login_required
def logout_user(request):
    logout(request)
    return render(request,'User_app/index.html')