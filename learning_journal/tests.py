"""Test file for all pyramid learning journal files."""
import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from learning_journal.models.mymodel import Journal
from learning_journal.models.meta import Base


@pytest.fixture(scope='session')
def configuration(request):
    """Set up a Configurator instance."""
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres://localhost:5432/test_learning_journal'
    })
    config.include("learning_journal.models")
    config.include("learning_journal.routes")

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture(scope='session')
def db_session(configuration, request):
    """Create a session for interacting with the test database."""
    SessionFactory = configuration.registry["dbsession_factory"]
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session


@pytest.fixture(scope='session')
def dummy_request(db_session):
    """Create a fake HTTP Request with a database session."""
    return testing.DummyRequest(dbsession=db_session)


def test_list_view_returns_dict(dummy_request):
    """Home page returns a response object."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)


def test_create_view_returns_dict(dummy_request):
    """New post page returns a response object."""
    from learning_journal.views.default import create_view
    response = create_view(dummy_request)
    assert isinstance(response, dict)


def test_detail_returning_dict_after_querying_db(dummy_request):
    """Test if detail view returns specific post from database."""
    from learning_journal.views.default import detail_view
    new_journal_post = Journal(
        id=1001,
        title='Stuff',
        created='2017-11-03',
        text='And things.'
    )
    dummy_request.dbsession.add(new_journal_post)
    dummy_request.dbsession.commit()
    dummy_request.matchdict['id'] = 1001
    response = detail_view(dummy_request)
    assert isinstance(response, dict)


def test_entry_exists_and_is_in_list_view(dummy_request):
    """Test if list view contains new journal post."""
    from learning_journal.views.default import list_view
    new_journal_post = Journal(
        title='test title',
        created='2017-12-12',
        text='This is some text.'
    )
    dummy_request.dbsession.add(new_journal_post)
    dummy_request.dbsession.commit()
    response = list_view(dummy_request)
    assert new_journal_post.to_dict() in response['entries']


def test_detail_view_returns_specific_entry_data(dummy_request):
    """Test if detail view returns specific contents of a fake post."""
    from learning_journal.views.default import detail_view
    new_journal_post = Journal(
        id=68,
        title='Hope this returns',
        created='2017-11-10',
        text='Lots of text here.'
    )
    dummy_request.dbsession.add(new_journal_post)
    dummy_request.dbsession.commit()
    dummy_request.matchdict['id'] = 68
    response = detail_view(dummy_request)
    assert response['entry']['title'] == 'Hope this returns'


def test_detail_view_non_existent_post(dummy_request):
    """Test if non-existent post raises HTTPNotFound."""
    from learning_journal.views.default import detail_view
    new_journal_post = Journal(
        title='test post',
        created='2017-11-01',
        text='text here.'
    )
    dummy_request.dbsession.add(new_journal_post)
    dummy_request.dbsession.commit()
    dummy_request.matchdict['id'] = 9009
    with pytest.raises(HTTPNotFound):
        detail_view(dummy_request)


def test_create_view_get_has_textarea_with_text(dummy_request):
    """Test create view goes to correct html page with placeholder text."""
    from learning_journal.views.default import create_view
    response = create_view(dummy_request)
    assert response == {'textarea': 'New Entry'}


def test_list_view_contains_new_entry(dummy_request):
    """Test if new entry data is in db."""
    from learning_journal.views.default import list_view
    new_journal_post = Journal(
        id=1010,
        title='Things',
        created='2017-11-10',
        text='Some great text.'
    )
    dummy_request.dbsession.add(new_journal_post)
    dummy_request.dbsession.commit()
    response = list_view(dummy_request)
    assert new_journal_post.to_dict() in response['entries']


def test_update_view_http_not_found(dummy_request):
    """Test if update raises HTTPNotFound on non-existent id."""
    from learning_journal.views.default import update_view
    dummy_request.matchdict['id'] = 250
    with pytest.raises(HTTPNotFound):
        update_view(dummy_request)


def test_update_view_get_returns_dict(dummy_request):
    """Test if update view returns a dictionary on get request."""
    from learning_journal.views.default import update_view
    new_entry = Journal(
        title='Things',
        text='Some great text.'
    )
    dummy_request.dbsession.add(new_entry)
    dummy_request.dbsession.commit()
    dummy_request.matchdict['id'] = 1
    response = update_view(dummy_request)
    assert isinstance(response, dict)


def test_create_view_on_post_redirects_home(dummy_request):
    """Test create view goes to home view after submit."""
    from learning_journal.views.default import create_view
    new_entry = {
        'title': 'New Stuff',
        'text': 'A short body.'
    }
    dummy_request.method = "POST"
    dummy_request.POST = new_entry
    response = create_view(dummy_request)
    assert isinstance(response, HTTPFound)


def test_notfound_returns_empty_dict(dummy_request):
    """Test if notfound view returns empty dictionary."""
    from learning_journal.views.notfound import notfound_view
    response = notfound_view(dummy_request)
    assert isinstance(response, dict)
