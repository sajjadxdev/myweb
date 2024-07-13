from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def myfunc(request):
    return render(request,'index.html')

def myfunc2(request):
    return render(request,'myform2.html')



