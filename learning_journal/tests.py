"""Test file for all pyramid learning journal files."""
from __future__ import unicode_literals
from pyramid import testing
from pyramid.httpexceptions import HTTPNotFound
import pytest


@pytest.fixture
def dummy_request():
    """Dummy request fixture to use throughout file."""
    return testing.DummyRequest()


@pytest.fixture
def testapp():
    """Test app fixture."""
    from webtest import TestApp
    from pyramid.config import Configurator

    def main():
        config = Configurator()
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
        return config.make_wsgi_app()

    app = main()
    return TestApp(app)


def test_list_view_returns_dict(dummy_request):
    """Home page returns a response object."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)


def test_list_view_returns_all_entries(dummy_request):
    """Home page returns all journal entries contained in data directory."""
    from learning_journal.views.default import list_view
    from learning_journal.data.entries import ENTRIES
    response = list_view(dummy_request)
    assert len(response['entries']) == len(ENTRIES)


def test_create_view_returns_dict(dummy_request):
    """New post page returns a response object."""
    from learning_journal.views.default import create_view
    response = create_view(dummy_request)
    assert isinstance(response, dict)


def test_detail_view_one_entry(dummy_request):
    """Detail page returns a response object with one journal."""
    from learning_journal.views.default import detail_view
    request = dummy_request
    request.matchdict['id'] = 879
    response = detail_view(request)
    assert '401 - Day 12' in response['entry']['title']


def test_detail_view_response_has_title(testapp):
    """Test detail_view response contains a title."""
    response = testapp.get('/journal/799')
    assert 'title' in response


def test_http_not_found(testapp):
    """Test if HTTPNotFound with bad route."""
    with pytest.raises(Exception):
        testapp.get("/journal/900")
