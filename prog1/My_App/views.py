from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request,"home.html")
def register(request):
    name=request.POST['name']
    password=request.POST['password']
    address=request.POST['address']
    email=request.POST['email']
    return render (request,"output.html",{'NAME':name,'PASSWORD':password,'ADDRESS':address,'EMAIL':email})