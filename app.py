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
# right now it list all quotes but this can be changed for the user to selecr based on status
@app.route('/get_quotes')
def get_quotes():
    return render_template("quote.html", quotes=mongo.db.quote.find())


@app.route('/add_task')
def add_task():
    return render_template(
        'addtask.html', categories=mongo.db.categories.find())


@app.route('/insert_task', methods=['POST'])
def insert_task():
    mongo.db.tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))


@app.route('/edit_quote/<quote_id>')
def edit_quote(quote_id):
    the_quote = mongo.db.quote.find_one({'_id': ObjectId(quote_id)})
    all_status = mongo.db.status.find()
    return render_template(
        'editquote.html', quote=the_quote, statuses=all_status)


@app.route('/update_quote/<quote_id>', methods=['POST'])
def update_quote(quote_id):
    mongo.db.quote.update(
        {'_id': ObjectId(quote_id)},
        {
            'quote_name': request.form.get('quote_name'),
            'category_name': request.form.get('category_name'),
            'quote_description': request.form.get('quote_description'),
            'due_date': request.form.get('due_date'),
            'is_urgent': request.form.get('is_urgent'),
        })
    return redirect(url_for('get_quotes'))


@app.route('/delete_quote/<quote_id>', methods=['POST'])
def delete_quote(quote_id):
    return 'Hello World ...delete task'
    # mongo.db.tasks.remove({'_id': ObjectId(task_id)})
    # return redirect(url_for('get_tasks'))


@app.route('/get_categories')
def get_categories():
    # return render_template('categories.html',
    #                        categories=mongo.db.categories.find())
    return 'Hello World ...category  '


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    # the_category = mongo.db.categories.find_one(
    #     {'_id': ObjectId(category_id)})
    # return render_template('editcategory.html', category=the_category)
    return 'Hello World ...category  '


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    # mongo.db.categories.update(
    #     {'_id': ObjectId(category_id)},
    #     {'category_name': request.form.get('category_name')})
    # return redirect(url_for('get_categories'))
    return 'Hello World ...category  '


@app.route('/delete_category/<category_id>', methods=['POST'])
def delete_category(category_id):
    # mongo.db.categories.remove({'_id': ObjectId(category_id)})
    # return redirect(url_for('get_categories'))
    return 'Hello World ...category  '


@app.route('/insert_category', methods=['POST'])
def insert_category():
    # category_doc = {'category_name': request.form.get('category_name')}
    # mongo.db.categories.insert_one(category_doc)
    # return redirect(url_for('get_categories'))
    return 'Hello World ...category  '


@app.route('/add_category')
def add_category():
    # return render_template('addcategory.html')
    return 'Hello World ...category  '


# this route was used to test and setup the connection
@app.route('/list_quotes')
def get_listquotes():
    # This connects to the db  quotes above to the quote collection and list all quotes
    return render_template("quoteslist.html", quotes=mongo.db.quote.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '127.0.0.1'),
            # port=int(os.environ.get('PORT', '8080')),
            port=5000,
            debug=True)
