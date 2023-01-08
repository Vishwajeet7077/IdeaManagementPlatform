from django.db import models
from account.models import Profile
from django.contrib.auth.models import User
from program.models import BusinessUnit, Program

# Create your models here.



class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='static/images/')
    business_unit = models.ForeignKey(
        BusinessUnit, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Pending')
    ideator = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    program = models.ForeignKey(Program, null=True, on_delete=models.SET_NULL)

    is_accepted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    is_on_hold = models.BooleanField(default=False)

    is_pending = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def accept(self):
        self.is_accepted = True
        self.is_rejected = False
        self.is_on_hold = False
        self.is_pending = False
        self.status = "Accepted"

    def reject(self):
        self.is_accepted = True
        self.is_rejected = False
        self.is_on_hold = False
        self.is_pending = False
        self.status = "Rejected"

    def putOnHold(self):
        self.is_accepted = True
        self.is_rejected = False
        self.is_on_hold = False
        self.is_pending = False
        self.status = "Put On Hold"
