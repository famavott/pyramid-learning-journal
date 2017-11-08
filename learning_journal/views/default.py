"""Module with view functions that serve each uri."""
from pyramid.view import view_config
from datetime import datetime
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from learning_journal.models.mymodel import Journal
from pyramid.security import remember, forget
from this_demoapp.security import check_credentials


@view_config(route_name='login', renderer='learning_journal:templates/login.jinja2')
def login(request):
    """Login view response for authentication."""
    if request.method == 'POST':
        username = request.params.get('username', '')
        password = request.params.get('password', '')
        if check_credentials(username, password):
            headers = remember(request, username)
            return HTTPFound(location=request.route_url('home'), headers=headers)
            return {}


@view_config(route_name='home', renderer='learning_journal:templates/index.jinja2')
def list_view(request):
    """Pass response to send to index.html page with all entries."""
    entries = request.dbsession.query(Journal).all()
    entries = [entry.to_dict() for entry in entries]
    return {
        'entries': entries
    }


@view_config(route_name='detail', renderer='learning_journal:templates/detail.jinja2')
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


@view_config(route_name='create', renderer='learning_journal:templates/new.jinja2')
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


@view_config(route_name='edit', renderer='learning_journal:templates/edit.jinja2')
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


@view_config(route_name='delete')
def delete_view(request):
    """Delete a specific entry."""
    target_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Journal).get(target_id)
    if entry:
        request.dbsession.delete(entry)
        return HTTPFound(request.route_url('home'))
    raise HTTPNotFound
