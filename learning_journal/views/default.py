"""Module with view functions that serve each uri."""
from pyramid.view import view_config
from datetime import datetime
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from learning_journal.models.mymodel import Journal
from pyramid.security import remember, forget, NO_PERMISSION_REQUIRED
from learning_journal.security import is_authenticated


@view_config(route_name='home', renderer='learning_journal:templates/index.jinja2', permission='view')
def list_view(request):
    """Pass response to send to index.html page with all entries."""
    entries = request.dbsession.query(Journal).all()
    entries = [entry.to_dict() for entry in entries]
    return {
        'entries': entries
    }


@view_config(route_name='detail', renderer='learning_journal:templates/detail.jinja2', permission='view')
def detail_view(request):
    """Pass response to send to detail page for individual entries."""
    target_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Journal).get(target_id)
    if not entry:
        raise HTTPNotFound
    if request.method == 'GET':
        return {
            'entry': entry.to_dict()
        }
    if request.method == "POST":
        return HTTPFound(request.route_url('edit', id=entry.id))


@view_config(route_name='create', renderer='learning_journal:templates/new.jinja2', permission='secret')
def create_view(request):
    """Pass response to send to new page."""
    if request.method == 'GET':
        return{
            'textarea': 'New Entry'
        }
    if request.method == 'POST':
        new_entry = Journal(
            title=request.POST['title'],
            text=request.POST['text'],
            created=datetime.now()
        )
        request.dbsession.add(new_entry)
        return HTTPFound(request.route_url('home'))


@view_config(route_name='edit', renderer='learning_journal:templates/edit.jinja2', permission='secret')
def update_view(request):
    """Pass response to send to edit page."""
    target_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Journal).get(target_id)
    if not entry:
        raise HTTPNotFound
    if request.method == 'GET':
        return {
            'entry': entry.to_dict()
        }
    if request.method == 'POST' and request.POST:
        entry.title = request.POST['title']
        entry.text = request.POST['body']
        entry.created = datetime.now()
        request.dbsession.add(entry)
        request.dbsession.flush()
        return HTTPFound(request.route_url('detail', id=entry.id))


@view_config(route_name='delete', permission='secret')
def delete_view(request):
    """Delete a specific entry."""
    target_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Journal).get(target_id)
    if entry:
        request.dbsession.delete(entry)
        return HTTPFound(request.route_url('home'))
    raise HTTPNotFound


@view_config(
    route_name='login', renderer="learning_journal:templates/login.jinja2", permission=NO_PERMISSION_REQUIRED
)
def login(request):
    """Login view config to authenticate username/password."""
    if request.authenticated_userid:
        return HTTPFound(request.route_url('home'))

    if request.method == "GET":
        return {}

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if is_authenticated(username, password):
            headers = remember(request, username)
            return HTTPFound(request.route_url('home'), headers=headers)

        return {
            'error': 'Invalid username/password combination.'
        }


@view_config(route_name='logout', permission=NO_PERMISSION_REQUIRED)
def logout(request):
    """Logout view config to redirect to home view."""
    headers = forget(request)
    return HTTPFound(request.route_url('home'), headers=headers)
