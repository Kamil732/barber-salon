from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

from accounts.models import Account

class Meeting(models.Model):
    TYPES = (
        ('hair', 'Włosy'),
        ('beard', 'Broda'),
    )

    customer = models.ForeignKey(verbose_name='Konto Klienta', to=Account, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='meetings')
    customer_first_name = models.CharField(verbose_name='Imię Klienta', max_length=20, blank=True)
    type = models.CharField(verbose_name='Typ Wizyty', max_length=5, choices=TYPES)
    start = models.DateTimeField(verbose_name='Wizyta jest o', unique=True)

    def __str__(self):
        return self.type

    def clean(self):
        if not(self.customer) and not(self.customer_first_name):
            raise ValidationError('Klient musi mieć imię')

        if Meeting.objects.filter(start__range=(self.start + timedelta(minutes=1), self.start + timedelta(minutes=29))).exists():
            raise ValidationError('Już istnieje wizyta o tej godzinie')

    def save(self, *args, **kwargs):
        if self.customer:
            self.customer_first_name = self.customer.first_name

        return super(Meeting, self).save(*args, **kwargs)