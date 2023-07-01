from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
# Create your models here.


class Userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    Address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)


class Meter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Serial_number = models.IntegerField(unique=True)
    Last_billed_reading = models.IntegerField()
    Last_recorded_reading = models.IntegerField()
    Last_updated_time = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(cascade_delete_history=True)
