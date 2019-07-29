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
def index():
    return render_template("index.html", page_title="Heh Welcome Y'all", page_heading="We are team of awesome designers making websites with Full Stack stuff", cta="Get Started", list_stuff_wedo=["Bootstrap", "Django", "Flask", "Python", "Javascript"])


@app.route('/get_quotes')
@app.route('/get_quotes/<status>')
def get_quotes(status='ALL'):
    # the status variable is passed in and I must figure out how to create the list
    # variable from all the documents in the status collection
    print(status)
    # This line finds all documents in qoutes collections and put them in the quotes variable
    # variable quotes passed back to quote.html file and it lists all quotes
    return render_template("getquotes.html", status=status, statuses=mongo.db.status.find(), quotes=mongo.db.quote.find())


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
    # qId = mongo.db.quote.find({"quoteId": {})
    # print(qId)
    # This function is losing the existing data so i must figure out how to change just the things we need
    # need to use updae $set and specify excactly tyhe ones i updayinfgupdating
    # all need to maintin same quoteId
    mongo.db.quote.update(
        {'_id': ObjectId(quote_id)},
        {
            "name": request.form.get("quote_name"),
            "email": request.form.get("quote_email"),
            "phone": request.form.get("quote_phone"),
            "rankQuality": request.form.get("quote_rankquality"),
            "rankTime": request.form.get("quote_ranktime"),
            "rankCost": request.form.get("quote_rankcost"),
            "levelQuality": request.form.get("quote_expectedquality"),
            "expectedDate": request.form.get("quote_expecteddate"),
            "liveDate": request.form.get("quote_livedate"),
            "budget": request.form.get("quote_budget "),
            "brief": request.form.get("quote_brief"),
            "typeDev": request.form.get("quote_typedev"),
            "tech": request.form.get("quote_tech"),
            "quoteStatus": request.form.get("quote_quotestatus"),
            "quoteDetails": request.form.get("quote_details"),
            "quoteResponse": request.form.get("quote_response"),
            "assignedTo": request.form.get("quote_person"),
            "quoteCost": request.form.get("quote_cost"),
            "quoteNeeds": request.form.get("quote_needs"),
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
    # do some ternanry work above
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
    app.run(host=os.environ.get('IP'),
            # to run in heroku uncomment this line and comment the port=5000 line
            port=int(os.environ.get('PORT')),
            # port=5000,
            debug=True)
