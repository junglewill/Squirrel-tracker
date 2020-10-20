from django.db import models

class Squirrel(models.Model):

    Latitude = models.FloatField(null=True)
    Longitude = models.FloatField(null=True)
    Unique_Squirrel_ID = models.CharField(max_length=1000, null=True)
    Shift = models.CharField(max_length=1000, null=True)
    Date = models.DateField(null=True)
    Age = models.CharField(max_length=1000, null=True)
    Primary_Fur_Color = models.CharField(max_length=1000, null=True)
    Location = models.CharField(max_length=1000, null=True)
    Specific_Location = models.CharField(max_length=1000, null=True)
    Running = models.BooleanField()
    Chasing = models.BooleanField()
    Climbing = models.BooleanField()
    Eating = models.BooleanField()
    Foraging = models.BooleanField()
    Other_Activities = models.CharField(max_length=1000, null=True)
    Kuks = models.BooleanField()
    Quaas = models.BooleanField()
    Moans = models.BooleanField()
    Tail_Flags = models.BooleanField()
    Tail_Twitches = models.BooleanField()
    Approaches = models.BooleanField()
    Indifferent = models.BooleanField()
    Runs_From = models.BooleanField()

# Create your models here.
