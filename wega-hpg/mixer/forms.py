from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import CheckboxInput

from calc.models import PlantProfile, PlantProfileHistory, PlantProfileShares
from mixer.models import Mixer

class MixerAddForm(forms.ModelForm):
    class Meta:
        model = Mixer
        fields = ['name', 'p1','p2','p3','p4','p5','p6','p7','p8']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control d-inline-block'

