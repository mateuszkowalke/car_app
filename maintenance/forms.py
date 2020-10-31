from django import forms
from .models import Car


class CarCreateForm(forms.ModelForm):

    class Meta:

        model = Car
        exclude = ('owner',)


class CarUpdateForm(forms.ModelForm):

    class Meta:

        model = Car
        exclude = ('owner',)
