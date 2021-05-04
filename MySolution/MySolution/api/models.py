from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Checking if number of lectures is positive
def is_positive(value):
    if value <= 0:
        raise ValidationError(
            _('%(value)s is incorrect number. There cannot be less than 1 lecture!'),
            params={'value': value},
        )


# Creating our courses model
class Courses(models.Model):
    name = models.CharField(verbose_name='name', max_length=75)
    start_date = models.DateField(verbose_name='start_date')
    end_date = models.DateField(verbose_name='end_date')
    lectures_num = models.PositiveIntegerField(
        verbose_name='lectures_num', validators=[is_positive])

    def __str__(self):
        return self.name
