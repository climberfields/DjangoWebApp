from django.conf.urls import url
# below we can see that we are telling it to pull from this app (.)
# import the views.py file
from . import views


#below we are seeing that it is saying in the views file
#import the object named index
urlpatterns = [
    url('', views.index, name='index')
]