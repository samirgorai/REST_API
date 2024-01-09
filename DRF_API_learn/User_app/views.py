from django.shortcuts import render
from django.contrib.auth.models import User
from User_app.forms import Create_user_form,Login_form
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
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
        user_form=Create_user_form(request.POST)
        if(user_form.is_valid()):
            #print('---------inside create_user3----------')
            #save user credentials           
            try:
                
                first_name=request.POST.get('first_name')
                last_name=request.POST.get('last_name')
                email=request.POST.get('email')
                username=request.POST.get('username')
                password=request.POST.get('password')
                #print('----------')
                print('first_name',first_name,"password:",password)
                User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)

                Flag=True
                #print('---------inside create_user4----------')
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
    
    if(request.method=="POST"):
        print('----------userlogin1-------')
        login_form=Login_form(request.POST)
        print("------login_form.is_valid()--------",login_form.is_valid(),"------------------")

        username = request.POST['username']
        password = request.POST['password']
        print("--------username:",username,"-----password-----",password)
        #user=authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        user=authenticate(request,username=username,password=password)
        print("----user-------",user,"-------------")
        if user is not None:
            login(request, user)
            return render(request, 'User_app/api_token_page.html', {'username': request.POST.get('username')})
            print('------ login success ---------')
        else:
            # Authentication failed
            return render(request, 'User_app/User_login.html', {'form': login_form})
            print('----------userlogin3-------')
    else:
        login_form=Login_form()                

    return render(request,'User_app/User_login.html',{"form":login_form})


