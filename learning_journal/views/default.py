"""Module with view functions that serve each uri."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from learning_journal.models.mymodel import Journal


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
    if request.method == 'GET':
        return {
            'entry': entry.to_dict()
        }
    if request.method == "POST":
        return HTTPFound(request.route_url('edit', id=entry.id))
    raise HTTPNotFound


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
            text=request.POST['text']
        )
        request.dbsession.add(new_entry)
        return HTTPFound(request.route_url('home'))


@view_config(route_name='edit', renderer='learning_journal:templates/edit.jinja2')
def update_view(request):
    """Pass response to send to edit page."""
    target_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Journal).get(target_id)
    if request.method == 'GET':
        return {
            'entry': entry.to_dict()
        }
    if request.method == 'POST' and request.POST:
        entry.title = request.POST['title']
        entry.text = request.POST['body']
        request.dbsession.add(entry)
        request.dbsession.flush()
        return HTTPFound(request.route_url('detail', id=entry.id))
