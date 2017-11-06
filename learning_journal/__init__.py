"""Init function to include routes and jinja2 files to make app."""
import os
from pyramid.config import Configurator


def main(gloabl_config, **settings):
    """Function returns a Pyramid WSGI application."""
    settings['sqlalchemy.url'] = os.environ.get(
        'DATABASE_URL', '')
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
