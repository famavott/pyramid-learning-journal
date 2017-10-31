"""View routes."""
import default


def includeme(config):
    """Add views for each view and provide route name."""
    config.add_view(list_view, route_name='home')
    config.add_view(detail_view, route_name='detail')
    config.add_view(create_view, route_name='create')
    config.add_view(update_view, route_name='edit')
