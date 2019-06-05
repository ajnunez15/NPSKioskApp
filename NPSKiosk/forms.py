from django import forms

class HomeForm(forms.Form):
    search = forms.CharField(label='')