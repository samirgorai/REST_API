from django.urls import path,include
from rest_framework import routers
from basic_api.views import UserViewset


router=routers.DefaultRouter()
router.register('employeeapi',UserViewset)


urlpatterns = [
    path('',include(router.urls)),
]