# AirBnB clone - The console

<p align="center">
    <img src="https://i.imgur.com/JOhaZ5m.png">
</p>

## Description

This team project is part of the Holberton School Full-Stack Software Engineer program.
It's the first step towards building a first full web application: an AirBnB clone.
This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data.

## Console and Command Usage

The console is a Unix shell-like command line user interface provided by the python [CmdModule](https://wiki.python.org/moin/CmdModule)
It prints a prompt and waits for the user for input, for our project we used **(hbnb)** 

Command | Example
------- | -------
Display commands help | ```(hbnb) help <command>```
Create object (prints its id)| ```(hbnb) create <class>```
Destroy object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
Show object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Show "all" objects or instances class | ```(hbnb) all``` or ```(hbnb) all <class>```
Run console | ```./console.py```
Quit console | ```(hbnb) quit```


Help command example

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
```

## Class Models Used


File | Description | Attributes
---- | ----------- | ----------
[base_model.py](./models/base_model.py) | BaseModel class for all the other classes | id, created_at, updated_at
[user.py](./models/user.py) | User class for future user information | email, password, first_name, last_name
[city.py](./models/city.py) | City class for future location information | state_id, name
[state.py](./models/state.py) | State class for future location information | name
[place.py](./models/place.py) | Place class for future accomodation information | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids
[review.py](./models/review.py) | Review class for future user/host review information | place_id, user_id, text
[amenity.py](./models/amenity.py) | Amenity class for future amenity information | name

## Tests

All the code is tested with the **unittest** module.
The test for the classes are in the [test_models](./tests/test_models/) folder.

## Authors

* **Marc Cavigli** - [718@holbertonschool.com](https://github.com/MCavigli)
* **Tywan Brooks** - [638@holbertonschool.com](https://github.com/tlvb25)