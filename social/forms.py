# social/forms.py
from django import forms
from django.contrib.auth.models import User

from .models import Post, UserProfile


class RegistrationForm(forms.Form):
    S_login = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'S-login'}))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password'}))


    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError('Passwords do not match')

        return password2

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'content']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'email', 'phone_number', 'image']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']