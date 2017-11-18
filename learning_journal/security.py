"""Configure and hold all security information for app."""
import os

from passlib.apps import custom_app_context as pwd_context

from pyramid.authentication import AuthTktAuthenticationPolicy

from pyramid.authorization import ACLAuthorizationPolicy

from pyramid.security import Allow, Authenticated, Everyone


class MyRoot(object):
    """MyRoot class to allow for access control list to be available to views."""

    def __init__(self, request):
        """Initialization for MyRoot class."""
        self.request = request

    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, Authenticated, 'secret')
    ]


def is_authenticated(username, password):
    """Check if user name and password are both validated."""
    stored_username = os.environ.get('AUTH_USERNAME')
    stored_password = os.environ.get('AUTH_PASSWORD')
    is_authenticated = False
    if stored_username and stored_password:
        if username == stored_username:
            try:
                is_authenticated = pwd_context.verify(password, stored_password)
            except ValueError:
                pass
    return is_authenticated


def includeme(config):
    """Security configuration settings for application."""
    auth_secret = os.environ.get('AUTH_SECRET', '')
    authn_policy = AuthTktAuthenticationPolicy(
        secret=auth_secret,
        hashalg='sha512'
    )
    config.set_authentication_policy(authn_policy)
    authz_policy = ACLAuthorizationPolicy()
    config.set_authorization_policy(authz_policy)
    config.set_default_permission('view')
    config.set_root_factory(MyRoot)


