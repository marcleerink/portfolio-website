from flask import Flask, render_template, url_for, send_file, request, redirect

app = Flask(__name__)
app.config.from_object('config')

to_do_list = {
    'sign-up': {'page' : 'Sign Up', 'priority' : 'Low', 'url' : 'sign-up'},
    'log-in': {'page' : 'Log In', 'priority' : 'Low', 'url' : 'log-in'},
    'contact': {'page' : 'Contact Form', 'priority' : 'Medium', 'url' : 'contact'},
    'projects': {'page' : 'Projects', 'priority' : 'High', 'url' : 'projects'},

}
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/software-engineer')
def software_engineer():
    return render_template('software_engineer.html')

@app.route('/sound-artist')
def sound_artist():
    return render_template('sound_artist.html')

@app.route('/contact-me')
def contact():  
    return render_template('contact_form.html')

@app.route('/projects')
def projects():  
    return render_template('projects.html')

@app.route('/cv')
def cv():
    return send_file('static/downloads/cv.pdf')

@app.route('/<slug>')
def pages(slug):
    if slug in to_do_list:
        return '<h2>'+ to_do_list[slug]['page'] + '</h2>' + '<p> Create a ' + to_do_list[slug]['page'] + ' Page <br> Priority: ' + to_do_list[slug]['priority'] + '</p>'
    else:
        return "Requested page does not excist"

@app.route('/to-do')
def todo():
    return render_template('to_do.html', todo = to_do_list)


if __name__ == '__main__':
    app.run()
