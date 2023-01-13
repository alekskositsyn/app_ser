from django.db import models
from django.core.validators import MaxValueValidator

from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=60)
    full_price = models.PositiveIntegerField()

    def __str__(self):
        return f'Name: {self.name}'


class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount')
    )
    plan_types = models.CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveIntegerField(default=0, validators=[
        MaxValueValidator(100)
    ])

    def __str__(self):
        return f'Discount : {self.plan_types} {self.discount_percent}%'


class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name='subscriptions', on_delete=models.PROTECT)
    services = models.ForeignKey(Service, related_name='subscription', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscription', on_delete=models.PROTECT)
