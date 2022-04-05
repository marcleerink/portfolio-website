from app.app import create_app
from app.software_engineer.models import Projects
from app.todo.models import Todo 
from app.extensions.database import db

app = create_app()
app.app_context().push()

to_do_list = {
    'sign-up': {'page' : 'Sign Up', 'priority' : 1},
    'log-in': {'page' : 'Log In', 'priority' : 1},
    'contact': {'page' : 'Contact Form', 'priority' : 2},
    'projects': {'page' : 'Projects', 'priority' : 3},
}

project_content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi scelerisque magna quis urna ultrices sodales. Donec rutrum nisl ac venenatis tempus. Donec molestie bibendum mauris, id luctus lacus consequat sit amet. Morbi facilisis luctus sem, et luctus est consectetur egestas. Nulla sed porttitor leo. Duis blandit odio vel arcu vehicula rutrum. Proin vitae leo a dui venenatis volutpat non at velit. Sed pulvinar elit eget dapibus dictum.'

projects_list = {
    'project-1': {'title' : 'Project 1', 'content': project_content, 'priority' : 1},
    'project-2': {'title' : 'Project 2', 'content': project_content, 'priority' : 2},
    'project-3': {'title' : 'Project 3', 'content': project_content, 'priority' : 2},
    'project-4': {'title' : 'Project 4', 'content': project_content, 'priority' : 2},
    'project-5': {'title' : 'Project 5', 'content': project_content, 'priority' : 2},
}
# for slug, todo in to_do_list.items():
#     new_todo = Todo(slug=slug, page=todo['page'], priority=todo['priority'])
#     db.session.add(new_todo)
    

for slug, project in projects_list.items():
    new_project = Projects(slug=slug, title=project['title'], content=project['content'], priority=project['priority'])
    db.session.add(new_project)

db.session.commit()