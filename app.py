#! /usr/local/bin/python

# Flask locally needs this above line to run as well as mods to the port number
# this is the test script to test connection to mongo connectmongo.py

import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'crm'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
# this function get the quotes and list them on the screeen
# right now it list all quotes but this can be changed for the user to select based on status
@app.route('/get_quotes')
def get_quotes():
    # This line finds all documents in qoutes collections and put them in the quotes variable
    # variable quotes passed back to quote.html file and it lists all quotes
    return render_template("getquotes.html", quotes=mongo.db.quote.find())

# This function displays the edit page and populates it with the document selected in quote.html
@app.route('/edit_quote/<quote_id>')
def edit_quote(quote_id):
    # Find the quote based on the unique quote_id
    the_quote = mongo.db.quote.find_one({'_id': ObjectId(quote_id)})
    all_status = mongo.db.status.find({})
    # nextquote = mongo.db.quotenumber.find()
    # print(nextquote)
    # print(all_status)
    # print(the_quote)
    return render_template(
        'editquote.html', quote=the_quote, statuses=all_status)


@app.route('/add_task')
def add_task():
    return 'Hello World ...not yet connected'
    # return render_template(
    # 'addtask.html', categories=mongo.db.categories.find())


@app.route('/insert_task', methods=['POST'])
def insert_task():
    mongo.db.tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))


@app.route('/update_quote/<quote_id>', methods=['POST'])
def update_quote(quote_id):
    # This function is losing the existing data so i must figure out how to change just the things we need
    # need to use updae $set and specify excactly tyhe ones i updayinfg
    mongo.db.quote.update(
        {'_id': ObjectId(quote_id)},
        {
            'quoteId': 44,
            'name': request.form.get('quote_name'),
            'brief': request.form.get('quote_brief'),
            'quoteStatus': request.form.get('quote_status'),
            'liveDate': request.form.get('live_date'),
            'isurgent': request.form.get('is_urgent'),
        })
    return redirect(url_for('get_quotes'))


@app.route('/delete_quote/<quote_id>', methods=['POST'])
def delete_quote(quote_id):
    return 'Hello World ...delete task'
    # mongo.db.tasks.remove({'_id': ObjectId(task_id)})
    # return redirect(url_for('get_tasks'))


# Status decorators and functions
# This section deals with the status collection of document in crm.status

@app.route('/get_status')
def get_status():
    # this is to list the quote status
    return render_template('getstatus.html', statuses=mongo.db.status.find())
    # return 'Hello World ...status '


@app.route('/delete_status/<status_id>', methods=['POST'])
def delete_status(status_id):
    # Deleting based on the document selected
    mongo.db.status.remove({'_id': ObjectId(status_id)})
    return redirect(url_for('get_status'))


@app.route('/edit_status/<status_id>')
def edit_status(status_id):
    # This find the selected document from the collection
    the_status = mongo.db.status.find_one(
        {'_id': ObjectId(status_id)})
    return render_template('editstatus.html', status=the_status)


@app.route('/update_status/<status_id>', methods=['POST'])
def update_status(status_id):
        # I want to make sure its always in upper case
    # I tried using |upper in jinja but it was not updating on the page
    quotestatus = request.form.get('quote_status')
    quotestatusupper = quotestatus.upper()
    mongo.db.status.update(
        {'_id': ObjectId(status_id)},
        {'quote_status': quotestatusupper})
    return redirect(url_for('get_status'))


@app.route('/insert_status', methods=['POST'])
def insert_status():
    # I want to make sure its always in upper case
    # I tried using |upper in jinja but it was not updating on the page
    quotestatus = request.form.get('quote_status')
    quotestatusupper = quotestatus.upper()
    status_doc = {'quote_status': quotestatusupper}
    mongo.db.status.insert_one(status_doc)
    return redirect(url_for('get_status'))


@app.route('/add_status')
def add_status():
    # adds new status on the addstatus page
    return render_template('addstatus.html')


# this route was used to test and setup the connection
@app.route('/list_quotes')
def get_listquotes():
    # This connects to the db  quotes above to the quote collection and list all quotes
    return render_template("quoteslist.html", quotes=mongo.db.quote.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '127.0.0.1'),
            port=int(os.environ.get('PORT', '8080')),
            # port=5000,
            debug=True)
  # set an environment variable to get around the problem im having with port on heroku and vscode
    #     port=os.getenv('PORT'),
    #     print(port),
