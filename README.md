# Squirrel-tracker
This is a website keeping track of all the known squirrels within Central Park, NYC. Through importing the <a href='https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw'>2018 Central Park Squirrel Census data</a>, the site allows user to add, update, and view squirrel data.

# Data Source & Management Command
The data source for this project is from <a href='https://opendata.cityofnewyork.us/'>NYC Open Data</a>. To import the data into the Django model, We'll use the following commands for importing data and exporting data in the terminal console:
```shell
python manage.py export_suqirrel_data path/to/file.csv
```
and
```shell
python manage.py import_suqirrel_data path/to/file.csv
```
Through running these commands, The database(sqlite) will be constructed with the open data and after the following web application functions, we can export the changes to another csv file for future usages.

# Web Application Functions

## Home page 
#### Located at /sightings/
Showing all the squirrel data in the database, with a button of <b>```View Details```</b> to check the detailed information of a specific squirrel

## Details
#### Located at /sightings/Unique_Squirrel_ID/
Displaying the detailed information of a specific squirrel, and followed with a blank field to update some certain values of the squirrel

## Add
#### Located at /sightings/add/
Adding new data to the database, with blank field to insert value and add

## Map
#### Located at /map/
Plotting the first 100 rows of squirrel data on the map based on their latitude and longitude data

## Statistics
#### Located at /sightings/stats
Calculating general statistics information for the database
