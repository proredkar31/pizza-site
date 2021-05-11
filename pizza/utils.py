from pymongo import MongoClient

def Collection(c):
    client = MongoClient("mongodb+srv://promodred31:fmmMnPkAQ4Lawg0Y@cluster0.osb9c.mongodb.net/test?retryWrites=true&w=majority")
    db = client["pizza"]
    collection= db["pizzas"]
    return collection


# pizza=    {
#         'name': 'Pramod',
#         'title': 'Pizza 1',
#         'description': 'First pizza content',
#         'date_created': 'August 27, 2018',
#         'toppings':'piza,piza,pizza,pizza',
#         'type':'Regular',
#         'size':'large',
#     }
# collection.insert_one(pizza)
