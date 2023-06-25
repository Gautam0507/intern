from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Meter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Serial_number = models.IntegerField(unique= True)
    Last_billed_reading = models.IntegerField()
    Last_recorded_reading = models.IntegerField()
    Last_updated_time = models.DateTimeField(auto_now=True)

