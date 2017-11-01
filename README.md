# Pyramid Learning Journal


A simple Pyramid app for my 401-Python learning journal.

**Authors**:

- Matt Favoino

## Routes:

- `/` - the home page and a listing of journals
- `/new-expense` - to create a new expense
- `/expense/{id:\d+}` - the page for an individual expense
- `/expense/{id:\d+}/edit` - for editing existing expenses
- `/expense/{cat:\w+}` - list all expenses by category

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
