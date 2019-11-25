
from django.forms import ModelForm

from .models import squirrel_data

# Create your views here.

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