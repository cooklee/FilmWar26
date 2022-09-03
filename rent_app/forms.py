from django import forms
from django.core.exceptions import ValidationError

from rent_app.models import Movie


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=10)


class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        widgets = {
            'category': forms.CheckboxSelectMultiple
        }

    def clean(self):
        data = super().clean()
        person = data['director']
        year = data['year']
        if person.year >= year:
            raise ValidationError("no nie !!!")
        return data