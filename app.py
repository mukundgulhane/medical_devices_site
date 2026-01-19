from flask import Flask, render_template

app = Flask(__name__)

# FRONT PAGE
@app.route('/')
def frontpage():
    return render_template('frontpage.html')

# INDEX PAGE - Electronics & IoT Topics
@app.route('/index')
def index():
    return render_template('index.html')

# CONTENT PAGES
@app.route('/components')
def components():
    return render_template('components.html')

@app.route('/circuit_building')
def circuit_building():
    return render_template('circuit_building.html')

@app.route('/measurements')
def measurements():
    return render_template('measurements.html')

@app.route('/fabrication')
def fabrication():
    return render_template('fabrication.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/cadprojects')
def cadprojects():
    return render_template('cadprojects.html')

@app.route('/firstpage')
def firstpage():
    return render_template('firstpage.html')

@app.route('/secondcontent') 
def secondcontent():
    return render_template('secondcontent.html')

@app.route('/contentone')
def contentone():
    return render_template('contentone.html')

app.run(debug=True)
