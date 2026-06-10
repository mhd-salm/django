from django.shortcuts import render
from django.http import HttpResponse

def add():
    x = 1
    y = 2
    return x

def sup(request):
    x = add()
    
    return render(request,'hello.html')
