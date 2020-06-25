from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'randomSecretKey@123'
socket = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def index():
    return render_template('index.html')


@socket.on('start_all')
def start_all():
    from function_start_all import start_all
    start_all()


if __name__ == '__main__':
    socket.run(app)