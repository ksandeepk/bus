from django.db import models

class PassengerRegModel(models.Model):
    cname = models.CharField(max_length = 200)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    membership_type = models.CharField(max_length = 100)


class BusModel(models.Model):
    bus_num = models.CharField(max_length = 10)
    bus_type = models.CharField(max_length = 50)
    source = models.CharField(max_length = 50)
    destination = models.CharField(max_length = 50)
    departure = models.DateTimeField()

    def __str__(self):
        return self.bus_num