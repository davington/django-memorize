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

from datetime import date, timedelta

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from algorithm import interval

class Practice(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    item = generic.GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User)
    next_practice = models.DateField(auto_now_add=True)
    times_practiced = models.PositiveIntegerField(default=1)
    easy_factor = models.FloatField(default=2.5)

    class Meta:
        ordering = ['next_practice']

    def set_next_practice(self, rating):
        days, ef = interval(self.times_practiced, rating, self.easy_factor)
        self.next_practice = date.today() + timedelta(days=days)
        self.times_practiced += 1
        self.easy_factor = ef

    def delay(self):
        self.next_practice = date.today() + timedelta(days=1)
