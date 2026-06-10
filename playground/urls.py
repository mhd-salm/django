#so what we doing in this module is
#we gonna MAP our URLs to our VIEW functions

# "." this means from the current folder ie "playground"
# we just importing the views.py so we can referance our functions in the view

from django.urls import path
from . import views


#so this is a URL configration module
urlpatterns = [
    path('hello/',views.sup)
]