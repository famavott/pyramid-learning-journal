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


## Step 3 Additions
- Added database interaction with sqlalchemy
- Changed views to query data from the database and pass as response
- Made changes to 404 page

## Step 3 Tests

---------- coverage: platform darwin, python 3.6.2-final-0 -----------
Name                                       Stmts   Miss  Cover   Missing
------------------------------------------------------------------------
learning_journal/__init__.py                  10      7    30%   8-15
learning_journal/data/__init__.py              0      0   100%
learning_journal/data/entries.py               2      0   100%
learning_journal/models/__init__.py           24      3    88%   46-49
learning_journal/models/meta.py                5      0   100%
learning_journal/models/mymodel.py            10      0   100%
learning_journal/routes.py                     6      0   100%
learning_journal/scripts/__init__.py           0      0   100%
learning_journal/scripts/initializedb.py      33     20    39%   27-30, 35-61
learning_journal/tests.py                     68      0   100%
learning_journal/views/__init__.py             0      0   100%
learning_journal/views/default.py             17      0   100%
learning_journal/views/notfound.py             4      2    50%   6-7
------------------------------------------------------------------------
TOTAL                                        179     32    82%

