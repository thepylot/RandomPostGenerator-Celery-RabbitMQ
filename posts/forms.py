from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class RandomPostGeneratorForm(forms.Form):
    number_of_posts = forms.IntegerField(
        validators=[
            MinValueValidator(50),
            MaxValueValidator(500)
        ]
    )