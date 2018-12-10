from django.shortcuts import render
#specific to this file we are telling it to import an HTTP response from
#django.http
from django.http import HttpResponse
# Create your views here.

#we have named the object 'index' to be sent to the URLs
# the index option houses the HTTP Response of HEY! as demonstrated as
# HTML language 
def index(request):
    return HttpResponse("<h2>HEY!</h2>")