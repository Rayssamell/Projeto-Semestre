from django import forms

from .models import Livro

class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = ('nome','autor','editora','anoPublicacao', 'isbn',
        'disciplina', 'quantidade', 'serieAlvo', 'imagem')
   
        widgets = {
            'nome': forms.TextInput(attrs={ 'class': 'form-control'}),
            'autor': forms.TextInput(attrs={ 'class': 'form-control'}),
            'editora': forms.TextInput(attrs={ 'class': 'form-control'}),
            'anoPublicacao': forms.TextInput(attrs={ 'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={ 'class': 'form-control'}),
            'disciplina':  forms.SelectMultiple(attrs={'class': 'form-control'}),
            'quantidade': forms.Textarea(attrs={ 'class': 'form-control'}),
            'serieAlvo': forms.TextInput({'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={ 'class': 'form-control'}),

        }