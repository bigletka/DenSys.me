from dataclasses import field
from django.forms import ModelForm
from .models import User
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.validators import RegexValidator


user = get_user_model

class UserCreateForm(forms.ModelForm):
    """
    Create user form
    """

    #email = forms.EmailField(label='email')
    #first_name = forms.CharField(label='first name', max_length=100)
    #last_name = forms.CharField(label='last name', max_length=100)
    #government_id = forms.CharField(label='government id', min_length=12,max_length=12)
    #phone_number = forms.CharField(label='Phone Number', validators=[RegexValidator(regex = r"^\+?1?\d{8,15}$")])
    class Meta:
        model = User
        fields = ('__all__')