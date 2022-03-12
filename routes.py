from flask import Blueprint, render_template


to_do_list = {
    'sign-up': {'page' : 'Sign Up', 'priority' : 'Low', 'url' : 'sign-up'},
    'log-in': {'page' : 'Log In', 'priority' : 'Low', 'url' : 'log-in'},
    'contact': {'page' : 'Contact Form', 'priority' : 'Medium', 'url' : 'contact'},
    'projects': {'page' : 'Projects', 'priority' : 'High', 'url' : 'projects'},

}

blueprint = Blueprint('to-do', __name__)

@blueprint.route('/<slug>')
def pages(slug):
    if slug in to_do_list:
        return '<h2>'+ to_do_list[slug]['page'] + '</h2>' + '<p> Create a ' + to_do_list[slug]['page'] + ' Page <br> Priority: ' + to_do_list[slug]['priority'] + '</p>'
    else:
        return "Requested page does not excist"

@blueprint.route('/to-do')
def todo():
    return render_template('todo/index.html', todo = to_do_list)