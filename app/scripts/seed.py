from app.app import create_app
from app.software_engineer.models import Projects
from app.extensions.database import db

app = create_app()
app.app_context().push()

# project1
project1_title = 'Portfolio Website'
project1_content = 'The portfolio website you are on right now. The frontend is build with custom HTML,CSS and JavaScript. The backend with Python/Flask.'
project1_link = 'https://marcleerink.herokuapp.com/'
project1_code_link = 'https://github.com/marcleerink/portfolio-website'
project1_image = '../static/images/portfolio_website.png'

# project2
project2_title = 'Live Performance Leveler'
project2_content = 'The Live Performance Leveler is a tool that can be used to automatically correct loudness of a live performance in real time. The Live Performance Leveler is software created in Max for Live. Please see the documentation with "View Project" for all information'
project2_link = 'https://github.com/marcleerink/Live-Performance-Leveler/blob/main/Documentation%20Live%20Performance%20Leveler%20V1.0.pdf'
project2_code_link = 'https://github.com/marcleerink/Live-Performance-Leveler'
project2_image = '../static/images/live-performance-leveler.png'

#project coming
project_title = 'Project'
project_content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi scelerisque magna quis urna ultrices sodales. Donec rutrum nisl ac venenatis tempus. Donec molestie bibendum mauris, id luctus lacus consequat sit amet. Morbi facilisis luctus sem, et luctus est consectetur egestas. Nulla sed porttitor leo. Duis blandit odio vel arcu vehicula rutrum. Proin vitae leo a dui venenatis volutpat non at velit. Sed pulvinar elit eget dapibus dictum.'
project_link = '#'
project_code_link = '#'
project_image = '../static/images/html.png'

projects_list = {
    'project-1': {'title' : project1_title, 'content': project1_content, 'link': project1_link, 'code_link' : project1_code_link, 'priority' : 1, 'image_url' : project1_image },
    'project-2': {'title' : project2_title, 'content': project2_content, 'link': project2_link, 'code_link' : project2_code_link, 'priority' : 2, 'image_url' : project2_image },
    'project-3': {'title' : project_title, 'content': project_content, 'link': project_link, 'code_link' : project_code_link, 'priority' : 2, 'image_url' : project_image },
    'project-4': {'title' : project_title, 'content': project_content, 'link': project_link, 'code_link' : project_code_link, 'priority' : 2, 'image_url' : project_image },
    'project-5': {'title' : project_title, 'content': project_content, 'link': project_link, 'code_link' : project_code_link, 'priority' : 2, 'image_url' : project_image },

}


for slug, project in projects_list.items():
    new_project = Projects(slug=slug, title=project['title'], content=project['content'], code_link=project['code_link'], priority=project['priority'], image_url=project['image_url'])
    db.session.add(new_project)

db.session.commit()