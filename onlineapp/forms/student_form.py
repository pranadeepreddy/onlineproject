from django import forms
from onlineapp.models import *


class AddStudent(forms.ModelForm):
    class Meta:
        model=Student
        exclude=['id','dob','college']
        widgets={

            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter name'}),

            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'enter email'}),

            'db_folder': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter dbname'}),

            'dropped_out': forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'droped out'}),

        }