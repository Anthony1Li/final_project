from django.db import models

# Create your models here.

class squirrel_data(models.Model):
    def __str__(self):
        return self.unique_squirrel_id
    latitude = models.FloatField()
    longitude= models.FloatField()
    unique_squirrel_id = models.CharField(max_length=200,unique=True)
    shift=models.CharField(max_length=200, null=True, blank=True)
    date=models.DateField(null=True, blank=True)
    age=models.CharField(max_length=200, null=True, blank=True)
    primary_fur_color=models.CharField(max_length=200, null=True, blank=True)
    location=models.CharField(max_length=200, null=True, blank=True)
    specific_location=models.CharField(max_length=200, null=True, blank=True)
    running=models.BooleanField()
    chasing=models.BooleanField()
    climbing=models.BooleanField()
    eating=models.BooleanField()
    foraging=models.BooleanField()
    other_activities=models.CharField(max_length=200, null=True, blank=True)
    kuks=models.BooleanField()
    quaas=models.BooleanField()
    moans=models.BooleanField()
    tail_flags=models.BooleanField()
    tail_twitches=models.BooleanField()
    approaches=models.BooleanField()
    indifferent=models.BooleanField()
    runs_from=models.BooleanField()
