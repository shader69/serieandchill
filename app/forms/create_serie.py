from django import forms
from app.models import Serie


class SerieCreationForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = [
            'title',
            'description',
            'rate',
            'director',
            'actor',
            'epNumb',
            'seasonNumb',
            'release',
            'nationalite',
            'categories',
            'photo'
        ]
