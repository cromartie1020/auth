from django.contrib import admin
from django.urls import path, include
from .views import Home
from example.views import ExampleView, home_view
from myapplication import views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', Home.as_view(), name='home'),
    path('example/',ExampleView.as_view(), name='example_home'),
    path('post/',home_view,name='home_view'),
    path('myapp/',views.hello, name='hello'),
    path('pages/',include('pages.urls')),
    path('logs/',include('logs.urls')),

]
