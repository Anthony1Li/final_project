from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .forms import squirrelForm
from django.db.models import Avg, Max, Min, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import squirrel_data

# Create your views here.
def sightings(request):
    sq_data=squirrel_data.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(sq_data, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'sightings/sightings.html', {'users':users})


def edit(request, unique_squirrel_id):
    edit_sighting = get_object_or_404(squirrel_data, unique_squirrel_id=unique_squirrel_id)
    if request.method == "POST":
        form = squirrelForm(request.POST, instance=edit_sighting)
        if form.is_valid():
            form.save()
            return redirect("/sightings/")
    form = squirrelForm(instance=edit_sighting)
    return render(request, "sightings/edit.html", {"form": form, "unique_squirrel_id":unique_squirrel_id})

def add(request):
    if request.method == "POST":
        form = squirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/sightings/")
    else:
        form = squirrelForm()
    return render(request, 'sightings/add.html', {'form':form})

def delete(request, unique_squirrel_id):
    del_sighting = squirrel_data.objects.filter(unique_squirrel_id=unique_squirrel_id)
    del_sighting.delete()
    return redirect(reverse('sightings:sightings'))

def stats(request):
    sq_data=squirrel_data.objects.all()
    a=len(sq_data)
    b=sq_data.aggregate(min_latitude=Min('latitude'),max_latitude=Max('latitude'),average_latitude=Avg('latitude'))
    c=sq_data.aggregate(min_longitude=Min('longitude'),max_longitude=Max('longitude'),average_longitude=Avg('longitude'))
    d=list(sq_data.values_list('shift').annotate(Count('shift')))
    e=list(sq_data.values_list('age').annotate(Count('age')))
    f=list(sq_data.values_list('primary_fur_color').annotate(Count('primary_fur_color')))
    return render(request, 'sightings/stats.html', {"a":a,"b":b,"c":c,"d":d,"e":e,"f":f})
