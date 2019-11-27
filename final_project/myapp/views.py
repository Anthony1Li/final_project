from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .forms import squirrelForm
from django.db.models import Avg, Max, Min

from .models import squirrel_data

# Create your views here.

def map(request):
   map_squirrel = squirrel_data.objects.all()[:100]
   return render(request, 'myapp/map.html', {"map_squirrel":map_squirrel})

def sightings(request):
   sq_data=squirrel_data.objects.all()
   return render(request, 'myapp/sightings.html', {'sq_data':sq_data})


def edit(request, unique_squirrel_id):
  edit_sighting= squirrel_data.objects.filter(unique_squirrel_id=unique_squirrel_id).first()
  if request.method == "POST":
    form = squirrelForm(request.POST, instance=edit_sighting)
    if form.is_valid():
      form.save()
      return redirect("/myapp/sightings/")
  form = squirrelForm(instance=edit_sighting)
  return render(request, "myapp/edit.html", {"form": form, "unique_squirrel_id":unique_squirrel_id})

def add(request):
   if request.method == "POST":
      form = squirrelForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("/myapp/sightings/")
   else:
      form = squirrelForm()
   return render(request, 'myapp/add.html', {'form':form})

def delete(request, unique_squirrel_id):
   del_sighting = squirrel_data.objects.filter(unique_squirrel_id=unique_squirrel_id)
   del_sighting.delete()
   return redirect(reverse('myapp:sightings'))

# def delete(request, unique_squirrel_id):
#    del_sighting = squirrel_data.objects.filter(unique_squirrel_id=unique_squirrel_id)
#    if request.method == 'POST':
#       del_sighting.delete()
#       return redirect("/myapp/sightings/")
#    return render(request, 'myapp/delete.html', {'del_sighting': del_sighting})

def stat(request):
   sq_data=squirrel_data.objects.all()

   a=sq_data.aggregate(min_latitude=Min('latitude'),max_latitude=Max('latitude'),average_latitude=Avg('latitude'))
   #sq_data.aggregate()
   #return HttpResponse("{{a}}")
   return render(request, 'myapp/stat.html', {"a":a})
