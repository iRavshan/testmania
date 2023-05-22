from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="Ismingiz", 
                                max_length=100, required=True,
                                widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ismingizni kiriting'}))
    last_name = forms.CharField(label="Familiya", max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Familiyangizni kiriting'}))
    username = forms.CharField(label="Foydalanuvchi nomi", 
                               max_length=100, required=True, 
                               widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Foydalanuvchi nomi yarating'}))

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'name': 'first_name',
            'id': 'first_name',
            'required': ''
        })
        self.fields['last_name'].widget.attrs.update({
            'name': 'last_name',
            'id': 'last_name',
            'required': ''
        })
        self.fields['username'].widget.attrs.update({
            'name': 'username',
            'id': 'username',
            'required': ''
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Parolni kiriting',
            'label': 'Parolni kiriting',
            'id': 'password1',
            'name': 'password1',
            'required': '',
            'help_text': ''
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Parolni kiriting',
            'label': 'Parolni qayta kiriting',
            'id': 'password1',
            'name': 'password1',
            'required': ''
        })
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

class UpdateProfile():
    pass