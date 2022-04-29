from django.db import models
from django.core.exceptions import ValidationError

def validate_positive(value):
    if value <= 0:
        raise ValidationError(f'{value} is not positive number')

class Offer(models.Model):
    bank_name = models.CharField(max_length=200)
    term_min = models.IntegerField(validators=[validate_positive])
    term_max = models.IntegerField(validators=[validate_positive])
    rate_min = models.FloatField(validators=[validate_positive])
    rate_max = models.FloatField(validators=[validate_positive])
    payment_min = models.IntegerField(validators=[validate_positive])
    payment_max = models.IntegerField(validators=[validate_positive])


