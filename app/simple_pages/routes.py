from flask import Blueprint, render_template, url_for, send_file, request, current_app

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def index():
    return render_template('simple_pages/index.html')

@blueprint.route('/sound-artist')
def sound_artist():
    return render_template('simple_pages/sound_artist.html')

@blueprint.route('/cv')
def cv():
    return send_file('static/downloads/cv.pdf')