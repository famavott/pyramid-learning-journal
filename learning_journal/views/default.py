"""Module with view functions that serve each uri."""

from pyramid.view import view_config
import os
import io


HERE = os.path.dirname(__file__)


@view_config(route_name='home', renderer='string')
def home_view(request):
    return "Home!"

@view_config(route_name='home', renderer='string')
def list_view(request):
    return

def list_view(request):
    """Serve all journal entries on home page."""
    path = os.path.join(HERE, '../templates/index.html')
    with io.open(path) as file:
        return Response(file.read())


def detail_view(request):
    """Serve detail HTML page for a single entry."""
    path = os.path.join(HERE, '../templates/detail.html')
    with io.open(path) as file:
        return Response(file.read())


def create_view(request):
    """Serve create entry HTML page."""
    path = os.path.join(HERE, '../templates/new.html')
    with io.open(path) as file:
        return Response(file.read())


def update_view(request):
    """Update existing journal entry."""
    path = os.path.join(HERE, '../templates/edit.html')
    with io.open(path) as file:
        return Response(file.read())
