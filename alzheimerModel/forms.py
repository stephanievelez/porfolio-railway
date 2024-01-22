#form implicitly validates what is being imputted

from django import forms
from .models import Alzheimer

class AlzheimerModel(forms.ModelForm):
    
    class Meta:
        model = Alzheimer
        fields = ['name', 'main_img']