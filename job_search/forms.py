from django import forms

class SearchBarForm(forms.Form):
    query = forms.CharField(label='', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Search for key terms - Ex: Software Engineer, Python, Java, Los Angeles, Texas, California...",
    })
    )