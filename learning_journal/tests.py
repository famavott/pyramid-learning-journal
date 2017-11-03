"""Test file for all pyramid learning journal files."""
from __future__ import unicode_literals
from pyramid import testing
import pytest


@pytest.fixture
def dummy_request():
    """Dummy request fixture to use throughout file."""
    return testing.DummyRequest()


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


def test_update_view_returns_dict(dummy_request):
    """Update post page returns a response object."""
    from learning_journal.views.default import update_view
    response = update_view(dummy_request)
    assert isinstance(response, dict)
