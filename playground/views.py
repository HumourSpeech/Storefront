from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# REQUEST HANDLER
# request->response

def say_hello(request):
    return render(request,'hello.html',{'name':'Nitin'})
    
