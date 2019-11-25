from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .forms import squirrelForm

from .models import squirrel_data

# Create your views here.

# def map(request):
#    return render(request, 'myapp/map.html', {})

def sightings(request):
   sq_data=squirrel_data.objects.all()
   return render(request, 'myapp/sightings.html', {'sq_data':sq_data})

# def edit(request, unque_squirrel_id):
#    sq_data=squirrel_data.objects.filter(unique_squirrel_id=unque_squirrel_id)
#    return render(request, 'myapp/edit.html', {})

def add(request):
   if request.method == "POST":
      form = squirrelForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("/sightings/")
   form = squirrelForm()
   return render(request, 'myapp/add.html', {'form':form})

# def stat(request):
#    return render(request, 'myapp/stat.html', {})