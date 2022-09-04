from django import forms
from django.contrib.auth.models import User
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


class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(max_length=128)
    password2 = forms.CharField(max_length=128)

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        data = super().clean()
        if data['password1'] != data['password2']:
            raise ValidationError("Hasła sie nie zgadzają")

        return data








