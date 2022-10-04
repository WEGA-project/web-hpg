from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import CheckboxInput

from calc.models import PlantProfile, PlantProfileHistory, PlantProfileShares
from mixer.models import Mixer


class PlantProfilePodgruzForm(forms.Form):
    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
       
        self.fields['model_from'].queryset = self.fields['model_from'].queryset.filter(user_id=current_user.id)
        for visible in self.visible_fields():
            if visible.name=='model_from':
                visible.field.widget.attrs['class'] = 'form-input'
            else:
                visible.field.widget.attrs['class'] = 'form-check-input d-inline-block'
     

    model_from    = forms.ModelChoiceField(PlantProfile.objects.all(), required=True, label="Выберите профиль")
    macro_udobr_persent   = forms.BooleanField(label = "Удобрения(соли) проценты макро",  required=False)
    micro_udobr_persent   = forms.BooleanField(label = "Удобрения(соли) проценты micro",  required=False)
    profile_macro = forms.BooleanField(label = "Профиль макро(N,P,K,...)",  required=False)
    profile_micro = forms.BooleanField(label=  "Профиль микро(Fe, B...)",  required=False)
    conc        = forms.BooleanField(label ="Концентраты",  required=False)
    mixer       = forms.BooleanField(label ="Изготовление",  required=False)
    # corrector   = forms.BooleanField(label ="Корректор")
    prices      = forms.BooleanField(label ="Вся вкладка Цена",  required=False)
    
class PlantProfileAddForm(forms.ModelForm):
    class Meta:
        model = PlantProfile
        fields = ['name', 'template']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control d-inline-block'
            if visible.name  not in  ['name', 'mixer']:
                visible.field.initial = 0
                visible.field.widget.attrs['required'] = True


 

class PlantProfileEditForm(forms.ModelForm):
    class Meta:
        model = PlantProfile
        exclude = ['user',   ]
    
    def __init__(self, *args, **kwargs):
        
        current_user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['mixer'].queryset = self.fields['mixer'].queryset.filter(user_id=current_user.id)
        
        for visible in self.visible_fields():
            
            if visible.name != 'name':
                # visible.field.widget.attrs['step'] = 1
                visible.field.widget.attrs['class'] = 'form-control d-inline-block precalc'
                visible.field.widget.attrs['inputmode'] = "decimal"
                visible.field.initial = 0
                visible.field.required = False
                
            if visible.name in PlantProfile.price_fields:
                visible.field.widget.attrs['step'] = 0.0001
                
            if visible.name == 'name':
                visible.field.widget.attrs['class'] = 'form-control d-inline-block col'
                
            if visible.name == 'calc_mode':
                visible.label= 'Макро метод расчета'

            if visible.name in ['p', 'cl']:
                visible.field.widget.attrs['class'] += ' hpg-green '
                
            if visible.name in ['litres']:
                visible.field.widget.attrs['min']='0.5'
                visible.field.widget.attrs['step'] = '0.5'

    
class DelForm(forms.Form):
    pass

                
class PlantProfileSharesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            if visible.name!='enabled':
                visible.field.widget.attrs['class'] = 'form-control '
                
            if visible.name=='link_name':
                visible.field.widget.attrs['pattern'] = '[A-z0-9_-]{3,100}'
                visible.field.widget.attrs['placeholder'] = 'ponicsru_lemon'
                
    class Meta:
        model = PlantProfileShares
        fields=[ 'link_name', 'enabled']

class FilterForm(forms.Form):
    hide_macro = forms.BooleanField(required=False, label='Спрятать макро')
    hide_micro = forms.BooleanField(required=False, label='Спрятать микро')
    hide_salt   = forms.BooleanField(required=False, label='Спрятать проценты')
    show_gramms = forms.BooleanField(required=False, label='Спрятать соли')
    

class PlantProfileUploadForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
 