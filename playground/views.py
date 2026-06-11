from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def sup(request):

    query_set = Product.objects.all()

    for i in query_set:
        print(i)
    return render(request,'hello.html')
