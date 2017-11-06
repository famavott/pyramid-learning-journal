"""Routes with names and uris associated."""


def includeme(config):
    """Include following route for static files and uris."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('detail', '/journal/{id:\d+}')
    config.add_route('create', '/journal/new-entry')
    config.add_route('edit', '/journal/edit-entry/{id:\d+}')
    config.add_route('delete', '/journal/delete/{id:\d+}')
