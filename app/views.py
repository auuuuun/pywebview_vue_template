import os
import webview

from functools import wraps
from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

# development path
gui_dir = os.path.join(os.path.dirname(__file__), '..', 'static')
if not os.path.exists(gui_dir):  # frozen executable path
    gui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
app = Flask(__name__, static_folder=gui_dir, template_folder=gui_dir)
# 替换flask和vue冲突的语法
app.jinja_env.variable_start_string = '{['
app.jinja_env.variable_end_string = ']}'

# Socket
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('connect', namespace='/message')
def handle_connect():
    emit('message', {'message': 'Client connected'}, broadcast=True)
    print('Client connected')


@socketio.on('message', namespace='/message')
def handle_message(json):
    message = json['message']
    emit('message', {'message': message}, broadcast=True)


def verify_token(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        token = request.headers.get('token')
        if token == webview.token:
            return function(*args, **kwargs)
        else:
            raise Exception('Authentication error')

    return wrapper


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response


@app.route('/')
def landing():
    """
    Render index.html. Initialization is performed asynchronously in initialize() function
    """
    return render_template('index.html', token=webview.token)


@app.route('/test_get')
@verify_token
def test_get():
    test = request.args['test']
    print(test)
    return jsonify({'status': '0'})


@app.route('/test_post', methods=['POST'])
@verify_token
def test_post():
    test = request.json['test']
    print(test)
    return jsonify({'status': '0'})
