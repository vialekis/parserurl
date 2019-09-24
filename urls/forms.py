from django import forms
from urls.models import URLItem

class UrlAddForm(forms.ModelForm):
    class Meta:
        model = URLItem
        fields = ('url', "key_word")
        labels = {"url":"URL","key_word":"Слово"}

class UrlAddForm2(forms.Form):
    url = forms.URLField(label="URL", initial='', required=True)
    key_word = forms.CharField(max_length=20,label="Слово", initial='', required=True)