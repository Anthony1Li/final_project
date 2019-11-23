from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import squirrel_data

# Create your views here.

def map(request):
   return render(request, 'myapp/map.html', {})

class sightings(generic.ListView):
   template_name = 'myapp/sightings.html'
   def get_queryset(self):
      return squirrel_data.objects.all()
   #return render(request, 'myapp/sightings.html', {})

class edit(generic.DetailView):
   model = squirrel_data
   template_name = 'myapp/edit.html'
   def get_queryset(self):
      return squirrel_data.objects.filter(unique_squirrel_id=unque_squirrel_id)
   #return render(request, 'myapp/edit.html', {})

def add(request):
   return render(request, 'myapp/add.html', {})

def stat(request):
   return render(request, 'myapp/stat.html', {})