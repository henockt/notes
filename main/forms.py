from django import forms

class TextForm(forms.Form):
    text = forms.CharField(label="text_form")
    title = forms.CharField(label="title")