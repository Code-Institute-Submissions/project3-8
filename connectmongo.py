#! /usr/local/bin/python


# Flask locally needs this above line to run as well as mods to the port number
# this is the test script to test connection to mongo connectmongo.py


import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

# dont forget to set this variable in Heroku config vars

mongo = PyMongo(app)


@app.route('/')
# this route was used to test and setup the connection
@app.route('/get_tasks')
def get_tasks():
    # This connects to the db  quotes above to the quote collection
    return render_template("quoteslist.html", quotes=mongo.db.quote.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            # to run in heroku uncomment this line and comment the port=5000 line
            # port=int(os.environ.get('PORT')),
            port=5000,
            debug=True)
