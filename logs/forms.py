from .models import Topic, Entry
from django import forms
class NewTopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['text',]

class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields=['topic','text']
        

