from django.shortcuts import render
from django.contrib.auth.models import User
from User_app.forms import Create_user_form,Login_form
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
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
    #print('---------inside create_user----------')
    if(request.method=="POST"):
        #print('---------inside create_user2----------')
        user_form=Create_user_form(data=request.POST)
        if(user_form.is_valid()):
            #print('---------inside create_user3----------')
            #save user credentials           
            
            """first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            email=request.POST.get('email')
            username=request.POST.get('username')
            password=request.POST.get('password')"""
            #print('----------')
            #print('first_name',first_name,"password:",password)
            #User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            Flag=True
            #print('---------inside create_user4----------')
            #User.first_name,User.last_name,User.username,User.email,User.password]
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
        print('----------userlogin1-------')
        login_form=Login_form(request.POST)
        print("------login_form.is_valid()--------",login_form.is_valid(),"------------------")
        if(login_form.is_valid()):
            #username = request.POST['username']
            #password = request.POST['password']
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            print("--------username:",username,"-----password-----",password)
            #user=authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
            user=authenticate(request,username=username,password=password)
            print("----user-------",user,"-------------")
            if user is not None:
                
                login(request, user)
                return render(request, 'User_app/api_token_page.html', {'username': request.POST.get('username')})
                print('------ login success ---------')
                authenticated=True
            else:
                # Authentication failed
                return render(request, 'User_app/User_login.html', {'form': login_form})
                print('----------userlogin3-------')
        login_form=Login_form()
    else:
        login_form=Login_form()                

    return render(request,'User_app/User_login.html',{"form":login_form,})

@login_required
def token_view(request):
    username=request.user
    token=''
    return(render(request,'User_app/api_token_page.html',{'username':username,'token':token}))

@login_required
def logout_user(request):
    logout(request)
    return render(request,'User_app/index.html')