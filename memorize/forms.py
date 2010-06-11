# Copyright 2010 Cristian Esquivias

# This file is part of django-memorize.

# django-memorize is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.

# django-memorize is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.

# You should have received a copy of the GNU General Public License
# along with django-memorize.  If not, see <http://www.gnu.org/licenses/>.

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
