# Pyramid Learning Journal


A simple Pyramid app for my 401-Python learning journal.

https://frightful-mausoleum-95099.herokuapp.com/

**Authors**:

- Matt Favoino

## Routes:

- `/` - the home page and a listing of journal entries
- `/detail/{id:\d+}` - the page for an individual entry
- `/journal/new-entry` - for adding a new entry
- `/{id:\d+}/edit-entry` - edit existing entry

## Set Up and Installation:

- Clone this repository to your local machine.

- Once downloaded, `cd` into the `pyramid_learning_journal` directory.

- Begin a new virtual environment with Python 3 and activate it.

- `cd` into the next `learning_journal` directory. It should be at the same level of `setup.py`

- `pip install` this package as well as the `testing` set of extras into your virtual environment.

- `$ pserve development.ini --reload` to serve the application on `http://localhost:6543`

## To Test

- If you have the `testing` extras installed, testing is simple. If you're in the same directory as `setup.py` type the following:

```
$ py.test pyramid_learning_journal

```

## Step 2 Additions

- Added jinja2 templating
- Changed view config to return a list of entries for the home route, and specific entry data for the detail
