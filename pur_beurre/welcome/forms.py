from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Produit'}), label='', max_length=100)