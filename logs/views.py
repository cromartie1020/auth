from django.shortcuts import render,HttpResponseRedirect
from .models import Topic, Entry
from .forms import NewTopicForm, EntryForm 
# Create your views here.
def logs(request):
    return render(request,'logs/logs.html')

def topics(request):
    t=Topic.objects.all()
    
    context ={'t':t}
    return render(request,'logs/topics.html',context)

def topic(request, id):
    t=Topic.objects.all()
    t=Topic.objects.get(pk=id) 
    entry=t.entry_set.all()
    context={'t':t,'entry':entry}
    return render(request,'logs/topic.html',context)




def NewTopicView(request):
    form = NewTopicForm(request.POST or None)
    if form.is_valid():
        form.save() 
        form=NewTopicForm()
    context={'form':form}
        
    return render(request,'logs/new_topic.html',context)      

    
    
def edit_entry(request, id):
    entry=Entry.objects.get(pk=id)
    
    topic=entry.topic
    
    form=EntryForm(instance=entry)

    form = EntryForm(request.POST or none)
    if form.is_valid():
        form =EntryForm(instance=entry)
    else:
        form =EntryForm(instance=entry, data=request.Post)
        return HttpResponseRedirect(reverse('topic',args=[topic.id]))

    context= {'entry': entry, 'topic':topic,'form':form}
    return render(request,'logs/edit_entry.html',context)

        
    
    context={
        'form':form
    }
    
     
    
    return render(request,'logs/edit_entry.html',context)


