from django.forms import ModelForm

from .models import Todo

class Todoforms(ModelForm):
    
    class Meta:
        
        model = Todo
        fields = "__all__"
