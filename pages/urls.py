from django.urls import path
from .views import *
urlpatterns =[
    path('',page,name='page'),   
    path('permalink/',pageview,name='pageview'),
]