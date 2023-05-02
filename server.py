from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/static/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/static/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

if __name__ == '__main__':
    app.run()

