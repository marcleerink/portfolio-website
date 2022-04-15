from app.app import create_app
from app.software_engineer.models import Projects
from app.extensions.database import db

app = create_app()
app.app_context().push()

# project1
project1_title = 'Portfolio Website'
project1_content = 'The portfolio website you are on right now. The frontend is build with custom HTML/CSS and JavaScript. The backend with Python/Flask.'
project1_link = '#'
project1_code_link = 'https://github.com/marcleerink/portfolio-website'
project1_image = '../static/images/portfolio_website.png'

#project coming
project_title = 'Project'
project_content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi scelerisque magna quis urna ultrices sodales. Donec rutrum nisl ac venenatis tempus. Donec molestie bibendum mauris, id luctus lacus consequat sit amet. Morbi facilisis luctus sem, et luctus est consectetur egestas. Nulla sed porttitor leo. Duis blandit odio vel arcu vehicula rutrum. Proin vitae leo a dui venenatis volutpat non at velit. Sed pulvinar elit eget dapibus dictum.'
project_link = '#'
project_code_link = '#'
project_image = '../static/images/html.png'

projects_list = {
    'project-1': {'title' : project1_title, 'content': project1_content, 'link': project1_link, 'code_link' : project1_code_link, 'priority' : 1, 'image_url' : project1_image },
    'project-2': {'title' : project_title, 'content': project_content, 'link': project_link, 'code_link' : project_code_link, 'priority' : 2, 'image_url' : project_image },
    'project-3': {'title' : project_title, 'content': project_content, 'link': project_link, 'code_link' : project_code_link, 'priority' : 2, 'image_url' : project_image },
    'project-4': {'title' : project_title, 'content': project_content, 'link': project_link, 'code_link' : project_code_link, 'priority' : 2, 'image_url' : project_image },
    'project-5': {'title' : project_title, 'content': project_content, 'link': project_link, 'code_link' : project_code_link, 'priority' : 2, 'image_url' : project_image },

}


for slug, project in projects_list.items():
    new_project = Projects(slug=slug, title=project['title'], content=project['content'], code_link=project['code_link'], priority=project['priority'], image_url=project['image_url'])
    db.session.add(new_project)

db.session.commit()