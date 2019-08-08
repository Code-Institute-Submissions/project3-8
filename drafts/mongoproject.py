import pymongo
import os

# MONGODB_URI = os.getenv("MONGO_URI")
MONGODB_URI = "mongodb+srv://ciaran:Code2019@quote-vj3wf.mongodb.net/quote?retryWrites=true&w=majority"
DBS_NAME = "quote"
COLLECTION_NAME = "quotenumber"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def get_record():
    print("")
    quoteNumber = input("Enter your quote number > ")
    # email = input("Enter email for quote > ")
    try:
        doc = coll.find_one({'quoteId': quoteNumber, })
        print(doc)
    except:
        print("Error accessing the database")
    if not doc:
        print("")
        print("Error! No Quote found.")
    return doc


def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("6. status Quote")
    print("7. add Quote #")
    print("5. Exit")

    option = input("Enter option: ")
    return option


def add_record():
    print("")
    # quoteId=add 1 to number of documents.
    # deleteing documents not allowed - status set to closed.
    # next version i will get the last used id.
    newQuoteId = str(1+coll.count_documents({}))
    name = input("Enter your name > ")
    email = input("Enter your email > ")
    liveDate = input("Enter live date  > ")
    # Put these into an array
    rankTime = input("Enter Time rank > ")
    rankQuality = input("Enter Quality rank > ")
    rankCost = input("Enter Cost rank > ")
    budget = input("Enter Budget > ")

    new_doc = {'quoteId': newQuoteId, 'name': name.title(), 'email': email, 'liveDate': liveDate,
               'rankTime': rankTime.upper(), 'rankQuality': rankQuality.upper(), 'rankCost':
               rankCost.upper(), 'budget': budget}

    try:
        coll.insert_one(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")


def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


def next_quoteno():
    lastQuote = coll.count_documents({})
    if lastQuote:
        print("got {}", lastQuote)
        newQuote = str(1+coll.count_documents({}))


def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")
                print(v)
                print(v.upper())

                if update_doc[k] == "":
                    update_doc[k] = v
                    print("update= {}", update_doc[k])

        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print(v)
            print(update_doc)
            print("Document updated")
        except:
            print("Error accessing the database")


def changestatus_record():
    # this function changes the quote status of a record
    print("in change")
    doc = get_record()
    print(doc)
    if doc:
        update_doc = {}
        print("")
        for k, v in doc.items():
            if k == "quoteStatus":
                print("here")
                print(v)
                # find the record and change the status to closed
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")

                if update_doc[k] == "":
                    update_doc[k] = v
                    print(update_doc)

        try:
            coll.update_one(doc, {'$set': update_doc})
            print(update_doc)
            print("")
            print("Quote updated")
        except:
            print("Error accessing the database")


def addid():
    # this function changes adds one to quote number
    print("in add id")
    thequotenumber = coll.find_one()
    # thequotenumber = mongo.db.quotenumber.find_one()
    print(thequotenumber)
    if thequotenumber:
        update_doc = {}
        print("")
        for k, v in thequotenumber.items():
            if k == "quotenumber":
                print("finding number")
                print(v)
                newqid = v+1
                update_doc[k] = newqid
                # find the record and change the status to closed
                # update_doc[k] = input(k.capitalize() + " [" + v + "] > ")
                # if update_doc[k] == "":
                #     update_doc[k] = v
                print(update_doc)
        try:
            coll.update_one(thequotenumber, {'$set': update_doc})
            print(update_doc)
            print("")
            print("Quote number updated")
        except:
            print("Error accessing the database")


def delete_record():

    doc = get_record()

    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())

        print("")
        confirmation = input(
            "Is this the document you want to delete?\nY or N > ")
        print("")

        if confirmation.lower() == 'y':
            try:
                coll.remove(doc)
                print("Document deleted!")
            except:
                print("Document not deleted")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "6":
            changestatus_record()
        elif option == "7":
            addid()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()
