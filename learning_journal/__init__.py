"""Init function to include routes and jinja2 files to make app."""
from pyramid.config import Configurator


def main(global_config, **settings):
    """Function returns a Pyramid WSGI application."""
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.routes')
    config.include('.models')
    #config.include('.views')
    config.scan()
    return config.make_wsgi_app()
