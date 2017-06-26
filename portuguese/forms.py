from django import forms

class WordForm(forms.Form):
    word_id = forms.IntegerField()
    translation = forms.CharField(required=False)
    is_known = forms.BooleanField(required=False)
