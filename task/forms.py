from django import forms 
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta: 
        model = TaskModel
        fields = '__all__'
        widgets = {
            'assign_date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'})
        }