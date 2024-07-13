from django.urls import path
from . import views

urlpatterns =[
    path('',views.myfunc),
    path('myform2',views.myfunc2,name='myform2')
]