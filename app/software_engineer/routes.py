from flask import Blueprint, render_template, request, current_app
from app import software_engineer
from .models import Projects

blueprint = Blueprint('software_engineer', __name__)
 
 
@blueprint.route('/software-engineer')
def software_engineer():
    page_number = request.args.get('page', 1, type=int)
    project_pagination = Projects.query.paginate(page_number, 2)
    return render_template('software_engineer/software_engineer.html', project_pagination = project_pagination)
    
@blueprint.route('/projects/<slug>')
def projects_page(slug):
    projects = Projects.query.filter_by(slug=slug).first_or_404()
    return render_template('software_engineer/show.html', projects=projects)

@blueprint.route('/projects')
def project():
    page_number = request.args.get('page', 1, type=int)
    project_pagination = Projects.query.paginate(page_number, current_app.config['PROJECTS_PER_PAGE'])
    return render_template('software_engineer/projects.html', project_pagination = project_pagination)