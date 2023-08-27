from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'autor', 'titulo_tag','texto']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título do Post'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'titulo_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag do Post'}),
            'texto': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','titulo_tag','texto']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título do Post'}),
            'titulo_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag do Post'}),
            'texto': forms.Textarea(attrs={'class': 'form-control'}),
        }