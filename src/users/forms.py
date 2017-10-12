from django import forms
from django.contrib import messages


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Username'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Password'}))


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Username'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': 'Email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Repeat password'}))

    '''def clean_password(self):
        data = self.cleaned_data
        if data.get('password') != data.get('password2'):
            raise forms.ValidationError("Las contraseñas no coinciden.")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data.get('password')'''


class UserForm(forms.Form):
    username = forms.CharField(required=False,
                               widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Username'}))
    first_name = forms.CharField(required=False,
                               widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'First name'}))
    last_name = forms.CharField(required=False,
                               widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Last name'}))
    email = forms.CharField(required=False,
                            widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': 'Email'}))
    password = forms.CharField(required=False,
                               widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Password'}))


class ProfileForm(forms.Form):
    avatar = forms.FileField(required=False,
                               widget=forms.FileInput(attrs={'class': "form-control-file", 'placeholder': 'Avatar'}))
    bio = forms.CharField(required=False,
                               widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': 'Bio'}))
