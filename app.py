#! /usr/local/bin/python
# Flask locally needs this above line to run on my local vscode server

import json
import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# Port and db name setin my local  env variables
app.config["MONGO_DBNAME"] = 'crm'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
mongo = PyMongo(app)

# This route loads index.html and sends in
# content for display on the hero image and about us.


@app.route('/')
def index():
    return render_template("index.html", page_title="Heh Welcome Y'all", page_heading="We are team of awesome designers making websites with Full Stack stuff", cta="Get Started", list_stuff_wedo=["Bootstrap", "Django", "Flask", "Python", "Javascript"])  # noqa


# this function get the quotes and list them on the screeen
# the page passes back the status variable
@app.route('/get_quotes')
@app.route('/get_quotes/<status>')
def get_quotes(status='ALL'):
    # the status variable is passed in and I create the list based on status
    # This finds all documents in qoutes collections and put them in quotes
    # variable and passed back to quote.html file and it lists all quotes
    return render_template("getquotes.html", status=status, statuses=mongo.db.status.find(), quotes=mongo.db.quote.find())  # noqa


# this function views a quotes
@app.route('/view_quote', methods=["GET", "POST"])
def view_quote():
    thequote = request.form.get('quote_id')

    if type(thequote) == type(None):
        quotedetails = "EMPTY"
        return render_template("viewquote.html",  quote=quotedetails)
    else:
        print("else")
        quote = int(thequote)
        print(quote)
        print(thequote)
        quotedetails = mongo.db.quote.find_one({"quoteId": quote})
        return render_template("viewquote.html",  quote=quotedetails)  # noqa


# This function displays the edit page with the input in quote.html
@app.route('/edit_quote/')
@app.route('/edit_quote/<quote_id>')
def edit_quote(quote_id):
    # Find the quote based on the unique quote_id
    the_quote = mongo.db.quote.find_one({'_id': ObjectId(quote_id)})
    all_status = mongo.db.status.find({})
    return render_template('editquote.html', quote=the_quote, statuses=all_status)  # noqa


@app.route('/add_quote')
def add_quote():
    return render_template('addquote.html')


@app.route('/insert_quote', methods=['POST'])
def insert_quote():
    # mongo.db.quote.insert_one(request.form.to_dict())
    # this part of the function get the old and generates new quote number
    thequotenumber = mongo.db.quotenumber.find_one()
    if thequotenumber:
        update_doc = {}
        for k, v in thequotenumber.items():
            if k == "quotenumber":
                newqid = v+1
                update_doc[k] = newqid
        try:
            mongo.db.quotenumber.update_one(
                thequotenumber, {'$set': update_doc})
            print("Quote number updated")
        except:
            print("Error accessing the database")

    # I want to make sure its always in upper case
    # I tried using |upper in jinja but it was not updating on the page

    quotename = request.form.get('quote_name')
    quotenametitle = quotename.title()
    quote_doc = {"quoteId": newqid,
                 'name': quotenametitle,
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
                 "quoteGdpr": request.form.get("quotegdpr"),
                 "quoteStatus": "NEW"
                 }

    mongo.db.quote.insert_one(quote_doc)
    # Tried to use flash but its not what i want, will fix this post on reload error in version 2
    # flash('You successfully added a project quote #')
    # return redirect(url_for('quotesuccess', quote=newqid))
    return render_template('quotesuccess.html', quote=newqid)


@app.route('/quotesuccess', methods=['GET'])
def quotesuccess(quote):
    return render_template('quotesuccess.html', quote)


@app.route('/update_quote/<quote_id>', methods=["GET", "POST"])
def update_quote(quote_id):
    mongo.db.quote.update(
        {'_id': ObjectId(quote_id)},
        {
            "quoteId": request.form.get("quote_quoteid"),
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
            "quoteStatus": request.form.get("quote_status"),
            "quoteDetails": request.form.get("quote_details"),
            "quoteResponse": request.form.get("quote_response"),
            "assignedTo": request.form.get("quote_person"),
            "quoteCost": request.form.get("quote_cost"),
            "quoteNeeds": request.form.get("quote_needs"),
            "quoteGdpr": request.form.get("quotegdpr"),
        })
    return redirect(url_for('get_quotes'))


@app.route('/delete_quote/<quote_id>')
def delete_quote(quote_id):
    # add in a are you sure break
    mongo.db.quote.remove({'_id': ObjectId(quote_id)})
    return redirect(url_for('get_quotes'))


# Status decorators and functions
# This section deals with the status collection of document in crm.status

@app.route('/get_status')
def get_status():
    # this is to list the quote status
    return render_template('getstatus.html', statuses=mongo.db.status.find())
    # return 'Hello World ...status '


@app.route('/delete_status/<status_id>')
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
    # do some ternary work above
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


# decorators for content pages

# The new quote  page take a post and flashes to a screen a thank you message.
# Plan to add this json post data to mongo DB file.
#
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form["name"])
        flash("Thats cool {},we got your note!" .format(request.form["name"]))
    return render_template("contact.html", heroimage="static/img/hero-contact.jpg", page_title="Touch base with us", page_heading="Book a coffee chat withn us, send a message or request a quote", cta="Let's do this")  # noqa

# Created a seperate page for the url_for tech pages.


@app.route('/tech')
def tech():
    data = []
    with open("./data/static.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("portfolio.html", page_title="We specalise in Full Stack Development", page_heading=" Our Technology Portfolio", cta="Run the APi now", staticMage=data)  # noqa

# this decorator is for pages called under tech
@app.route('/tech/<member_name>', methods=["GET", "POST"])
def about_member(member_name):
    member = {}
    with open("data/static.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    # return "<h1>"+member["name"]+"</h1>"
    return render_template("member.html", member=member)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            # PORT variable now set in bash so no need for this
            # port=5000,
            # Dont forget to change before deployment
            debug=True)
