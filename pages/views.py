from django.shortcuts import render
from .forms import PageForm
from django import forms
from .models import Page
def page(request):

    first=Page.objects.all()
    context={'first':first}
    return render(request,'pages/home.html',context)

def pageview(request):
    form=PageForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        form=PageForm()
    context={'form':form}
    
    return render(request,'pages/page.html',context)    

