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

- A view that shows a map that displays the location of the squirrel sightings on an OpenStreets map.   
   >Located at: /map   
	Method: GET   
	Will use the https://leafletjs.com/ library for plotting

- A view that lists all squirrel sightings with links to edit and add sightings   
    >Located at: /sightings   
Method: GET   
A view to update a particular sighting   
Located at: /sightings/<unique-squirrel-id>
Method: POST  
 
- A view to create a new sighting   
    >Located at: /sightings/add   
Method: POST   

- A view to delete a sighting    
    >Located at: /sightings/<unique-squirrel-id>   
Method: DELETE   

- A view with general stats about the sightings
Particular stats are for you to decide but must include five of the attributes listed in the initial CSV download.    
    >Located at: /sightings/stats   
Method: GET   



## Dependencies
- [Django](https://www.djangoproject.com)
- [django-leaflet](https://django-leaflet.readthedocs.io/en/latest/)


## Documentation
The official description for this project is [**Squirrel Tracker**](https://docs.google.com/document/d/1SPv3fMDKiemrR86rD-S9ecvI2npz3PljDzwCfxK2x5g/edit)

## Background
Eccentric billionaire Joffrey Hosencratz just purchased the web development company you work for. You’ve met him once in an elevator and he was impressed with your skill in developing web applications with the ``Django`` framework. He also relayed that his most recent trip to Sedona, AZ has left him in a bit of trouble. See, he fancies the show Rick and Morty and a particular scene coupled with a traumatic childhood squirrel experience and a bad crystal bath experience in Sedona as left him wanting. 

He would like to start keeping track of all the known squirrels and plans to start with Central Park. He’s asked you to build an application that can import the 2018 Central Park Squirrel Census data and allow his team to add, update, and delete squirrel data. 



## Discussion and Development
Most development discussion is taking place on github in this repo.

## Contributing to Squirrel Tracker 

All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome.


## Contributors

Group Name: Project Group 29

Section: 2

Contributors: Jiyao Li, Hanyu Wu

UNIs: [jl5551, hw2753]