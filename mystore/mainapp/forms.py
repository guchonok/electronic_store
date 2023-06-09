from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:33em;'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width:33em;'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width:33em;'}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'style': 'width:33em;'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'from-control', 'background': 'red;'}),
            'password1': forms.PasswordInput(attrs={'class': 'from-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'from-input'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 250px;'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'placeholder': '********', 'class': 'form-control',
                                                                 'style': 'width: 250px;'}))


class UpdateProfileForm(forms.ModelForm):
    model = Profile
    name = forms.CharField(label='Имя', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:29em;'}))
    surname = forms.CharField(label='Фамилия', required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:29em;'}))
    phone = forms.CharField(label='Номер телефона', required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:29em;'}))
    avatar = forms.ImageField(label='Аватарка', required=False,
                              widget=forms.FileInput(attrs={'class': 'form-control', 'style': 'width:29em;'}))

    class Meta:
        model = Profile
        fields = ['name', 'surname', 'phone', 'avatar']


class SellProduct(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['title', 'description', 'short_description', 'cost', 'photo', 'category', 'tags', ]
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 10}),
            'short_description': forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(SellProduct, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['style'] = 'width:42em; border: 3px solid; background:#ced4da;'
