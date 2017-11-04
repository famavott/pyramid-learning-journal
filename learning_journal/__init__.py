"""Init function to include routes and jinja2 files to make app."""
from pyramid.config import Configurator


def main():
    """Function returns a Pyramid WSGI application."""
    config = Configurator()
    config.include('pyramid_jinja2')
    config.include('.routes')
    config.include('.models')
    config.scan()
    return config.make_wsgi_app()
