from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Username'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Password'}))


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Username'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': 'Email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Repeat password'}))
