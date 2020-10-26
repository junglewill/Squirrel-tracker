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

