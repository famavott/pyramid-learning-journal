"""Test file for all pyramid learning journal files."""
from __future__ import unicode_literals
from pyramid import testing
import pytest


@pytest.fixture
def dummy_request():
    """Dummy request fixture to use throughout file."""
    return testing.DummyRequest()


def test_list_view_response_status_code_200(dummy_request):
    """."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert response.status_code == 200


def test_detail_view_response_status_code_200(dummy_request):
    """."""
    from learning_journal.views.default import detail_view
    response = detail_view(dummy_request)
    assert response.status_code == 200


def test_create_view_response_status_code_200(dummy_request):
    """."""
    from learning_journal.views.default import create_view
    response = create_view(dummy_request)
    assert response.status_code == 200


def test_create_update_response_status_code_200(dummy_request):
    """."""
    from learning_journal.views.default import update_view
    response = update_view(dummy_request)
    assert response.status_code == 200


def test_list_view_response_is_html(dummy_request):
    """."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert response.concent_type == 'text/html'


def test_list_view_response_has_proper_content(dummy_request):
    """."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    the_tag = '<h2>401 Learning Journal Journal</h2>'
    assert the_tag in response.ubody
