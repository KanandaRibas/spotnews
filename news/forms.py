from django import forms
from news.models.news_model import News


class CreateCategoriesForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=200)


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        labels = {
            "title": "Título",
            "content": "Conteúdo",
            "author": "Autoria",
            "created_at": "Criado em",
            "image": "URL da Imagem",
        }
        widgets = {
            "content": forms.Textarea,
            "created_at": forms.DateInput(attrs={"type": "date"}),
            "image": forms.FileInput,
            "categories": forms.CheckboxSelectMultiple,
        }
