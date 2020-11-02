from django.shortcuts import render
from django.views.generic import View
from .forms import ExampleForm
from .models import Example
# Create your views here.

class ExampleView(View):

    def get(self, request):
        form=ExampleForm()
        
        first=Example.objects.all()
        content={'form':form,"first":first}
        return render(request,'example/home.html',content)    

def home_view(request):
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        form.save() 
        form=ExampleForm()
    context={'form':form}
        
    return render(request,'example/example.html',context)  