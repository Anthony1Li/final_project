from django.db import models

# Create your models here.

class squirrel_data(models.Model):
    def __str__(self):
        return self.unique_squirrel_id
    latitude = models.FloatField(null=False, blank=False)
    longitude= models.FloatField(null=False, blank=False)
    unique_squirrel_id = models.CharField(max_length=200,unique=True,null=False, blank=False)
    shift=models.CharField(max_length=200, null=True, blank=True)
    date=models.DateField(null=True, blank=True)
    age=models.CharField(max_length=200, null=True, blank=True)
    primary_fur_color=models.CharField(max_length=200, null=True, blank=True)
    location=models.CharField(max_length=200, null=True, blank=True)
    specific_location=models.CharField(max_length=200, null=True, blank=True)
    running=models.BooleanField(null=True, blank=True)
    chasing=models.BooleanField(null=True, blank=True)
    climbing=models.BooleanField(null=True, blank=True)
    eating=models.BooleanField(null=True, blank=True)
    foraging=models.BooleanField(null=True, blank=True)
    other_activities=models.CharField(max_length=200, null=True, blank=True)
    kuks=models.BooleanField(null=True, blank=True)
    quaas=models.BooleanField(null=True, blank=True)
    moans=models.BooleanField(null=True, blank=True)
    tail_flags=models.BooleanField(null=True, blank=True)
    tail_twitches=models.BooleanField(null=True, blank=True)
    approaches=models.BooleanField(null=True, blank=True)
    indifferent=models.BooleanField(null=True, blank=True)
    runs_from=models.BooleanField(null=True, blank=True)
