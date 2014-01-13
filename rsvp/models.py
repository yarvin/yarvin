from django.db import models

class Guest(models.Model):
    name = models.CharField(max_length=200)
    attendance = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()

    def __str__(self):
        return self.name
