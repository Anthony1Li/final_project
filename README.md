# Squirrel Tracker: a visulization web-application of tracking squirrels


## What is it?

**Squirrel Tracker** This is a web-application constructed based on Django to manage import, manipulate and visualize sightings data of squirrels found in central park of New York.


## Data Source
We use squirrel data [**2018 Central Park Squirrel Census**](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) which was counted by the [**Squirrel Census**](https://www.thesquirrelcensus.com/). 

This data set contains data from 3,023 sightings, including location coordinates, age, primary and etc..


## Management Commands
Import: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command. 

```sh
python manage.py import_squirrel_data /path/to/file.csv
```

Export: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command.

```sh
python manage.py export_squirrel_data /path/to/file.csv
```

## API

- ###Map View    
[Map View](https://project-261004.appspot.com/map/)   is a view that shows a map that displays the location of the squirrel sightings on an OpenStreets map.   
    >Located at: /map   
	 Method: GET   
	 Use the [leaflet](https://leafletjs.com/) library for plotting   

- ###Squirrel Lists View   
[Lists View](https://project-261004.appspot.com/sightings/) is a view that lists all squirrel sightings with links to edit and add sightings   
    >Located at: /sightings   
	Method: GET   
	
- ###Squirrel Update View   
[Update View](https://project-261004.appspot.com/sightings/13E-AM-1017-05/) is a view to update a particular sighting.    
    >Located at: /sightings/<unique-squirrel-id>   
	Method: GET & POST   

 
- ###Squirrel Create View   
[Create View](https://project-261004.appspot.com/sighitngs/add/) is a view to create a new sighting   
    >Located at: /sightings/add   
	Method: GET & POST   

- ###Squirrel Delete View   
[Delete View](https://project-261004.appspot.com/sightings/13E-AM-1017-05/) is a view to delete a sighting    
    >Located at: /sightings/<unique-squirrel-id>   
	Method: DELETE   

- ###Squirrel Stats View   
[Stats View](https://project-261004.appspot.com/sightings/stats/) is a view with general stats about the sightings
Stats include five of the attributes listed in the initial CSV download.    
    >Located at: /sightings/stats   
Method: GET   



## Dependencies
- [Django](https://www.djangoproject.com)
- [Django-Leaflet](https://django-leaflet.readthedocs.io/en/latest/)  
 
More information in [**Requeirments**](https://github.com/Anthony1Li/final_project/blob/master/requirements.txt)

## Documentation
The official description for this project is 
[**Squirrel Tracker**](https://docs.google.com/document/d/1SPv3fMDKiemrR86rD-S9ecvI2npz3PljDzwCfxK2x5g/edit)

## Background
Eccentric billionaire Joffrey Hosencratz just purchased the web development company you work for. You’ve met him once in an elevator and he was impressed with your skill in developing web applications with the ``Django`` framework. He also relayed that his most recent trip to Sedona, AZ has left him in a bit of trouble. See, he fancies the show Rick and Morty and a particular scene coupled with a traumatic childhood squirrel experience and a bad crystal bath experience in Sedona as left him wanting. 

He would like to start keeping track of all the known squirrels and plans to start with Central Park. He’s asked you to build an application that can import the 2018 Central Park Squirrel Census data and allow his team to add, update, and delete squirrel data. 



## Discussion and Development
Most development discussion is taking place on github in this repo.



## Contributors

Group Name: Project Group 29

Section: 2

Contributors: Jiyao Li, Hanyu Wu

UNIs: [**[jl5551]**](https://github.com/Anthony1Li), [**[hw2753]**](https://github.com/harrywoo)

[**Link**](https://project-261004.appspot.com/sightings) to our Squirrel Tracker application.
