"""Module with view functions that serve each uri."""

from pyramid.response import Response
from pyramid.view import view_config
import os
import io


HERE = os.path.dirname(__file__)


def list_view(request):
    """Serve all journal entries on home page."""
    path = os.path.join(HERE, '../templates/index.html')
    with io.open(path) as file:
        file.read()
    return Response(file)


def detail_view(request):
    """Serve detail HTML page for a single entry."""
    path = os.path.join(HERE, '../templates/detail.html')
    with io.open(path) as file:
        file.read()
    return Response(file)


def create_view(request):
    """Serve create entry HTML page."""
    path = os.path.join(HERE, '../templates/new.html')
    with io.open(path) as file:
        file.read()
    return Response(file)


def update_view(request):
    """Update existing journal entry."""
    path = os.path.join(HERE, '../templates/edit.html')
    with io.open(path) as file:
        file.read()
    return Response(file)
