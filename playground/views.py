from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q,F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def sup(request):

    #product = Product.objects.filter(Q(inventory__lt=10) | Q(price__gt=20))

    product = Product.objects.filter()
    
    return render(request,'hello.html',{'name':'salman','prices': list(product)})
