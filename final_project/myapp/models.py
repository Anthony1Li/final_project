from django.db import models

# Create your models here.


class squirrel_data(models.Model):
    def __str__(self):
        return self.unqiue_squirrel_id
    latitude = models.FloatField()
    longitude= models.FloatField()
    unqiue_squirrel_id = models.CharField(max_length=200)
    #hectare=models.CharField(max_length=200)
    shift=models.CharField(max_length=200)
    date=models.DateField()
    #hectare_squirrel_number=models.IntegerField()
    age=models.CharField(max_length=200)
    primary_fur_color=models.CharField(max_length=200)
    #highlight_fur_color=models.CharField(max_length=200)
    #combination_of_primary_and_highlight_color=models.CharField(max_length=200)
    #color_notes=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    #above_ground_sighter_measurement=models.CharField(max_length=200)
    specific_location=models.CharField(max_length=200)
    running=models.BooleanField()
    chasing=models.BooleanField()
    climbing=models.BooleanField()
    eating=models.BooleanField()
    foraging=models.BooleanField()
    other_activities=models.CharField(max_length=200)
    kuks=models.BooleanField()
    quaas=models.BooleanField()
    moans=models.BooleanField()
    tail_flags=models.BooleanField()
    tail_twitches=models.BooleanField()
    approaches=models.BooleanField()
    indifferent=models.BooleanField()
    runs_from=models.BooleanField()
    #other_interaction=models.CharField(max_length=200)
    #lat_long=models.CharField(max_length=200)

