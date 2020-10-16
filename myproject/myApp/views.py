from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import Webpage, AccessRecord, Topic, User
# Create your views here.


def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    # my_dict = {'insert_me' : "Hello I am from myApp."}
    return render(request, 'myApp/index.html', context=date_dict) 

def users(request):
     
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request, 'myApp/users.html',context=user_dict)