from django.db import models


class Clients(models.Model):
    full_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    number = models.CharField(max_length=15)
    event_date = models.DateField()
    event_type = models.CharField(max_length=100)
    guest_count = models.IntegerField(max_length=1000)
    info = models.TextField(null=True, blank=True)

