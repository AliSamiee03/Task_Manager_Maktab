from django import forms
from .models import Task

class CheckboxForm(forms.ModelForm):
    class Meta:
        model= Task
        fields = ['done']
        
        