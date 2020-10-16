from django.conf.urls import url
from myApp import views

urlpatterns = [
    url(r'^$',views.users,name='users'),
]