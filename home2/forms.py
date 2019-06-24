from django import forms
from home2.models import Book,Author,Genre

class BookForms(forms.Form):
    name = forms.CharField(label ='Book Name',
        widget = forms.TextInput(attrs={'maxlength':'30','placeholder':'Book Name',
        'class':'form-control'}))
    author = forms.ModelChoiceField(
                    queryset=Author.objects.all(),
                    empty_label='Author',widget=forms.Select(attrs={'name':'author','id':'author',
                    'class':'custom.select'}))
  
    genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),
                            widget=forms.CheckboxSelectMultiple)
    pur_date = forms.DateField(label='',
                            widget = forms)
    
