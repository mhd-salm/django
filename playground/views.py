from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q,F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product,OrderItem

                                                               

def sup(request):

    #product = Product.objects.filter(Q(inventory__lt=10) | Q(price__gt=20))

    items = Product.objects.filter(id__in=OrderItem.objects.values_list('product_id').distinct()).order_by('title')


    itemsa = Product.objects.filter(id__in=OrderItem.objects.values('product_id')).distinct().order_by('title') 
    product = Product.objects.order_by('title')
    return render(request,'hello.html',{'name':'salman','prices': list(itemsa)})
