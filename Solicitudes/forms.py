from django import forms
from django.forms import ModelForm
from .models import Solicitud143_Step1b, Solicitud143_Step1, Solicitud143_Step2

class FormStepOne(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms. CharField(max_length=100)
    email = forms.EmailField()

class FormStepTwo(forms.Form):
    job = forms.CharField(max_length=100)
    salary = forms.CharField(max_length=100)
    job_description = forms.CharField(widget=forms.Textarea)

class SolicitudesStep1_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step1
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 1'
        label='Solicitudes: Step 1'

class SolicitudesStep1b_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step1b
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 1b'
        label='Solicitudes: Step 1b'

class SolicitudesStep2_Form(forms.ModelForm):
    class Meta:
        model=Solicitud143_Step2
        fields = '__all__'
        exclude = ('estado','uc','um',)
        verbose_name='Solicitudes: Step 2'
        label='Solicitudes: Step 2'