from django.db import models

# Create your models here.

class squirrel_data(models.Model):
    def __str__(self):
        return self.unqiue_squirrel_id
    latitude = models.FloatField()
    longitude= models.FloatField()
    unqiue_squirrel_id = models.CharField(max_length=200)
    shift=models.CharField(max_length=200)
    date=models.DateField()
    age=models.CharField(max_length=200)
    primary_fur_color=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
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

class squirrelForm(ModelForm):
     class Meta:
         model = squirrel_data
         fields = ['latitude',
         'longitude',
         'unqiue_squirrel_id',
         'shift',
         'date',
         'age',
         'primary_fur_color',
         'location',
         'specific_location',
         'running',
         'chasing',
         'climbing',
         'eating',
         'foraging',
         'other_activities',
         'kuks',
         'quaas',
         'moans',
         'tail_flags',
         'tail_twitches',
         'approaches',
         'indifferent',
         'runs_from']