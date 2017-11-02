"""Module with view functions that serve each uri."""

from pyramid.view import view_config


@view_config(route_name='home', renderer='learning_journal:templates/index.jinja2')
def list_view(request):
    """Pass response to send to index.html page."""
    pass


@view_config(route_name='detail', renderer='learning_journal:templates/detail.jinja2')
def detail_view(request):
    """Pass response to send to detail.html page."""
    pass


@view_config(route_name='create', renderer='learning_journal:templates/new.jinja2')
def create_view(request):
    """Pass response to send to new.html page."""
    pass


@view_config(route_name='edit', renderer='learning_journal:templates/edit.jinja2')
def update_view(request):
    """Pass response to send to edit.html page."""
    pass
