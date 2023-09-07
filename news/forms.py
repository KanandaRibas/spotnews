from django import forms


class CreateCategoriesForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=200)
