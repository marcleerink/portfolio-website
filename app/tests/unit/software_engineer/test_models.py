import pytest
from app.extensions.database import db
from app.software_engineer.models import Projects


def test_projects_model_update (client):
    # updates projects properties
    projects = Projects(slug='project-20', title = 'Project 20', content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi scelerisque magna quis urna ultrices sodales. Donec rutrum nisl ac venenatis tempus. Donec molestie bibendum mauris, id luctus lacus consequat sit amet. Morbi facilisis luctus sem, et luctus est consectetur egestas. Nulla sed porttitor leo. Duis blandit odio vel arcu vehicula rutrum. Proin vitae leo a dui venenatis volutpat non at velit. Sed pulvinar elit eget dapibus dictum.')
    db.session.add(projects)
    db.session.commit()

    projects.page = 'Project 2'
    projects.save()

    updated_projects = Projects.query.filter_by(slug='project-20').first()
    assert updated_projects.title == 'Project 20'

def test_projects_delete(client):
    # deletes projects
    projects = Projects(slug='project-1', title = 'Project 1', content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi scelerisque magna quis urna ultrices sodales. Donec rutrum nisl ac venenatis tempus. Donec molestie bibendum mauris, id luctus lacus consequat sit amet. Morbi facilisis luctus sem, et luctus est consectetur egestas. Nulla sed porttitor leo. Duis blandit odio vel arcu vehicula rutrum. Proin vitae leo a dui venenatis volutpat non at velit. Sed pulvinar elit eget dapibus dictum.')
    db.session.add(projects)
    db.session.commit()

    projects.delete()

    deleted_projects = projects.query.filter_by(slug='project-1').first()
    assert deleted_projects is None
