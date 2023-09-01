from django import forms
from .models import Post, Categoria

categorias_query = Categoria.objects.all().values_list('nome','nome')
categorias = []
for item in categorias_query:
    categorias.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'autor', 'titulo_tag','categoria','texto']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título do Post'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'cat', 'type':'hidden'}),
            # 'autor': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(choices= categorias, attrs={'class': 'form-control'}),
            'titulo_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag do Post'}),
            'texto': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','titulo_tag','categoria','texto']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título do Post'}),
            'titulo_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag do Post'}),
            'texto': forms.Textarea(attrs={'class': 'form-control'}),
            'categoria': forms.Select(choices= categorias, attrs={'class': 'form-control'}),
        }