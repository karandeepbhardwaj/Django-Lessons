from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    my_dict = {'insert_me' : "Hello I am from myApp."}
    return render(request, 'myApp/index.html', context=my_dict) 