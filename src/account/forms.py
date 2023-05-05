from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    def __init__(self):
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'name': 'firstname',
            'id': 'firstname',
            'type':'text',
            'required': '',
            'placeholder': 'Ismingizni kiriting'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'name': 'lastname',
            'id': 'lastname',
            'type':'text',
            'required': '',
            'placeholder': 'Familiyangizni kiriting'
        })
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
