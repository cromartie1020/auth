from .models import Example
from django import forms
class ExampleForm(forms.ModelForm):
    class Meta:
        model=Example
        fields=['name','text']
