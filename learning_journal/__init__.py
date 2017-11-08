"""Init function to include routes and jinja2 files to make app."""
import os
from pyramid.config import Configurator


def main(gloabl_config, **settings):
    """Function returns a Pyramid WSGI application."""
    if os.environ.get('DATABASE_URL', ''):
        settings['sqlalchemy.url'] = os.environ['DATABASE_URL']
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.include('.security')
    config.scan()
    return config.make_wsgi_app()
