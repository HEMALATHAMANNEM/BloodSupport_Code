from django.forms import ModelForm
from django import forms
from .models import Donor

class DonorForm(ModelForm):
    class Meta:
        model=Donor
        fields='__all__'

        widgets={
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'},render_value=True),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'bloodgroup':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
        }

