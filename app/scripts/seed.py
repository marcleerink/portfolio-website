from app.app import create_app
from app.software_engineer.models import Projects
from app.extensions.database import db

app = create_app()
app.app_context().push()

project_content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi scelerisque magna quis urna ultrices sodales. Donec rutrum nisl ac venenatis tempus. Donec molestie bibendum mauris, id luctus lacus consequat sit amet. Morbi facilisis luctus sem, et luctus est consectetur egestas. Nulla sed porttitor leo. Duis blandit odio vel arcu vehicula rutrum. Proin vitae leo a dui venenatis volutpat non at velit. Sed pulvinar elit eget dapibus dictum.'
project_image = '../static/images/html.png'

projects_list = {
    'project-1': {'title' : 'Project 1', 'content': project_content, 'priority' : 1, 'image_url' : project_image },
    'project-2': {'title' : 'Project 2', 'content': project_content, 'priority' : 2, 'image_url' : project_image },
    'project-3': {'title' : 'Project 3', 'content': project_content, 'priority' : 2, 'image_url' : project_image },
    'project-4': {'title' : 'Project 4', 'content': project_content, 'priority' : 2, 'image_url' : project_image },
    'project-5': {'title' : 'Project 5', 'content': project_content, 'priority' : 2, 'image_url' : project_image },
}


for slug, project in projects_list.items():
    new_project = Projects(slug=slug, title=project['title'], content=project['content'], priority=project['priority'])
    db.session.add(new_project)

db.session.commit()