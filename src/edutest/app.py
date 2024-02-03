from flask import Flask

from .constants import SUCCESSFUL_INCREASE_MSG

app = Flask(__name__)
counter = 0 # not a constant ; pylint: disable=invalid-name

@app.route('/')
def index():
    return 'ok'

@app.route('/inc', methods=['POST'])
def increase():
    global counter
    current_counter = counter
    counter += 1
    return {
        'msg': SUCCESSFUL_INCREASE_MSG,
        'prev': current_counter,
        'new': counter
    }, 201
