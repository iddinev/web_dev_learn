from bottle import Bottle, run, get, static_file

app = Bottle()

@app.route('/')
def index():
    return static_file('index.html', root='.')

@app.route('/favicon.ico')
def icon():
    return static_file('assets/images/favicon.ico', root='.')

@app.route("/assets/images/<filename>")
def img(filename):
    return static_file(filename, root='assets/images')

@app.route("/assets/styles/<filename>")
def style(filename):
    return static_file(filename, root='assets/styles')

@app.route("/assets/fonts/<filename:path>")
def font(filename):
    return static_file(filename, root='assets/fonts')

@app.route("/assets/scripts/<filename:path>")
def script(filename):
    return static_file(filename, root='assets/scripts')

run(app, host='localhost', port=8080, reloader=True)
