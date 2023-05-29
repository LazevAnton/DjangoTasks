from django import forms
from django.forms import TextInput, Textarea

from TasksAPP.models import Tasks


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['task_title', 'task_description']
        widgets = {
            'task_title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type title'
            }),
            'task_description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type description'
            }),
        }
