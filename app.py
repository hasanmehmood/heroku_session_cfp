import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from {}'.format(os.getenv('VAR_1'))
