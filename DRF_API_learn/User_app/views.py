from django.shortcuts import render
from django.contrib.auth.models import User
from User_app.forms import Create_user_form
# Create your views here.

#home 
def index(request):
    return render(request,'User_app/index.html')


#create_user
def create_user(request):
    Flag=False
    message=''
    user_form=Create_user_form()
    print('---------inside create_user----------')
    if(request.method=="POST"):
        print('---------inside create_user2----------')
        user_form=Create_user_form(request.POST)
        if(user_form.is_valid()):
            print('---------inside create_user3----------')
            #save user credentials           
            try:
                
                first_name=request.POST.get('first_name')
                last_name=request.POST.get('last_name')
                email=request.POST.get('email')
                username=request.POST.get('username')
                password=request.POST.get('password')
                print('----------')
                print('first_name',first_name)
                User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)

                Flag=True
                print('---------inside create_user4----------')
                #User.first_name,User.last_name,User.username,User.email,User.password]           
                return render(request,'User_app/createusersuccess.html',{'username':username,'fname':first_name,'Lname':last_name})
            except:
                message="User profile not Created"
            
            message="Succcesfully Created User profile"
        else:
            message="User profile not Created"
    else:
        message=''
    return render(request,'User_app/create_user.html',{"form":user_form})  

    
def user_login(request):
    return render(request,'User_app/User_login.html')