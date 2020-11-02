from django.shortcuts import render, redirect
import datetime
def hello(request):
    day=datetime.datetime.now().date()
    time=datetime.datetime.now().time()
    weekday = datetime.datetime.now().weekday()

    dWeek=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturdy','Sunday']
    weekday=dWeek[weekday]
    context={

        'dWeek':dWeek,
        'day':day,
        'time':time,
        'weekday':weekday
    }
    return render(request,'myapplication/home.html',context)


    
