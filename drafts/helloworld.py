#! /usr/local/bin/python
# Ciarans template on flask needs this above line to run as well as mods to the port number
import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World ...Heroku connected'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            # to run in heroku uncomment this line and comment the port=5000 line
            port=int(os.environ.get('PORT')),
            # port=5000,
            debug=True)
