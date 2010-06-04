from django import forms
from django.core.exceptions import ValidationError

def validate_0_5(value):
    if not 0 <= value <= 5:
        raise ValidationError

RATINGS = ((0, 'Blanked'), (1, 'Barely Know It'), (2, 'Needs Work'),
           (3, 'Remembered'), (4, 'Solid'))

class RatingsForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)
    rating = forms.ChoiceField(choices=RATINGS)
