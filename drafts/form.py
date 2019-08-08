#! /usr/local/bin/python
# Ciarans template on flask needs this above line to run as well as mods to the port number
from flask import Flask, render_template, Response, request, redirect, url_for
import os
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('login.html')


def move_forward():
    # Moving forward code
    print("Moving Forward...")
    return 'Hello World ...move connected'


//rendering the HTML page which has the button
@app.route('/json')
def json():
    return render_template('json.html')


//background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print "Hello"
    return "nothing"


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            # to run in heroku uncomment this line and comment the port=5000 line
            # port=int(os.environ.get('PORT')),
            port=5000,
            debug=True)
