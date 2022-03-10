from flask import Flask
from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/software-engineer')
def software_engineer():
    return render_template('software_engineer.html')

@app.route('/sound-artist')
def sound_artist():
    return render_template('sound_artist.html')

if __name__ == '__main__':
    app.run()