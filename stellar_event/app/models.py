from django.db import models


class Clients(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=80)
    mobile_number = models.CharField(max_length=15)


class Event(models.Model):
    doe = models.DateField()
    event_type = models.CharField(max_length=100)
    guest_nr = models.IntegerField(max_length=100000)
    event_info = models.TextField(null=True, blank=True)

# dy databaza nji per klientet nje per eventet e organizuara
