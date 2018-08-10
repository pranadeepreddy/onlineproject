from django import forms
from onlineapp.models import *


class AddCollege(forms.ModelForm):

    class Meta:
        model=College
        exclude=['id']
        widgets={

            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'enter college name'}),

            'location': forms.TextInput(attrs={'class':'form-control','placeholder':'enter location'}),

            'acronym':forms.TextInput(attrs={'class':'form-control','placeholder':'enter acronym'}),

            'contact': forms.EmailInput(attrs={'class':'form-control','placeholder':'enter contact'}),

        }