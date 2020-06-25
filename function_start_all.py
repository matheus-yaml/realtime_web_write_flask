from flask_socketio import emit
from time import sleep


def start_all():
    for c in range(10):
        emit('start_all', f'{c}\n')
        sleep(1)
