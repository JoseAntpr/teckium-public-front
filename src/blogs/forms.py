from django import forms
from django.contrib import messages


class CommentForm(forms.Form):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': "form-control content", 'placeholder': 'Escribe un comentario', 'rows':'3'}))


class PostForm(forms.Form):

    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control content", 'placeholder': 'Titulo'}))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': "form-control-file"}))
    summary = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': "form-control content", 'placeholder': 'Escribe un resumen ', 'rows':'3'}))
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': "form-control content", 'placeholder': 'Cuenta tu historia', 'rows':'6'}))
    blogs = forms.ChoiceField(required=False, choices=())
    tags = forms.MultipleChoiceField(choices=(), widget=forms.SelectMultiple(attrs={'class': "form-control content"}))

    def __init__(self, *args, **kwargs):
        tag_list = kwargs.pop('tags')
        blog_list = kwargs.pop('blogs')
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['tags'] = forms.MultipleChoiceField(required=False, choices=[(t.get('id'), t.get('name')) for t in tag_list], widget=forms.SelectMultiple(attrs={'class': "form-control"}))
        self.fields['blogs'] = forms.ChoiceField(choices=[(b.get('id'), b.get('title')) for b in blog_list], widget=forms.Select(attrs={'class': "form-control"}))
