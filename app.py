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

if __name__ == "__main__":
    app.run(debug=True)
