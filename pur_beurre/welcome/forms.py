from django import forms

class SearchForm(forms.Form):
    research = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Produit'}), label='', max_length=100)