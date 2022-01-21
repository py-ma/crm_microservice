from django.forms import ModelForm
from .models import ModelsForm

class Form(ModelForm):
    class Meta:
        model = ModelsForm
        fields = '__all__'
        
