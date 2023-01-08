from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BusinessUnit(models.Model):
    name = models.CharField(max_length=200)
    jury = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)

    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    application_start_time = models.DateTimeField(null=True)
    application_end_time = models.DateTimeField(null=True)

    coordinator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    business_unit = models.ForeignKey(BusinessUnit, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name