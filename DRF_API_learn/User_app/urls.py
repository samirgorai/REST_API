from django.urls import path
from User_app import views

app_name='User_app'

urlpatterns=[
    path('createuser/',views.create_user,name='createuser'),
    path('userlogin/',views.user_login,name='user_login'),
    path('token/',views.token_view,name='token'),
]