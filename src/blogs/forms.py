from django import forms
from django.contrib import messages

class CommentForm(forms.Form):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': 'Escribe un comentario', 'rows':'3'}))