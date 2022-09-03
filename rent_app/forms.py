from django import forms

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