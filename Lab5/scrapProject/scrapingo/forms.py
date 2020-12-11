from django import forms

class Form(forms.Form):
    url = forms.CharField()
    typ = forms.CharField()