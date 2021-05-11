from django.shortcuts import render,redirect
from django.http  import HttpResponse
import time
from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
#from pymongo import 

def error_404_view(request,exception):
    return render(request,'404.html')

def mongoCollection(table):
    client = MongoClient("mongodb+srv://promodred31:fmmMnPkAQ4Lawg0Y@cluster0.osb9c.mongodb.net/test?retryWrites=true&w=majority")
    db = client["pizza"]
    col= db[table]
    return col

def addSize(size):
    collection=mongoCollection('sizes')
    collection.insert_one({'size':size})

def home(request):
    collection=mongoCollection('pizzas')
    pizzas = list(collection.find())
    p=pizzas
    for pizza in p:
        pizza['id'] = pizza.pop('_id')
    collection=mongoCollection('sizes')
    sizes = list(collection.find())
    sizes=[size['size'] for size in sizes]

    if request.method=='POST':
        filtered_pizzas=[pizza for pizza in pizzas if pizza['size']==request.POST.get('size') and pizza['type']==request.POST.get('type')]
        #print(filtered_pizzas)
        return render(request,'pizza/home.html',{'pizzas':filtered_pizzas,'sizes':sizes})
        #collection=mongoCollection('pizzas')
    else:
        #pizzas = list(collection.find())
        #print(sizes)
        return render(request,'pizza/home.html',{'pizzas':pizzas,'sizes':sizes})

def createPizza(request):

    if request.method =='POST' :
        if request.POST.get("add_size"):
            addSize(request.POST.get("add_size"))
            return redirect(createPizza)
        else:
            collection=mongoCollection('pizzas')
            ts = time.time()
            date_time = datetime.fromtimestamp(int(ts))
            date_time=date_time.strftime('%B %d, %Y')
            pizza={
                'name': request.POST.get('name') ,
                'title': request.POST.get('title') ,
                'description':  request.POST.get('description'),
                'date_created':date_time ,
                'toppings':  request.POST.get('toppings'),
                'type': request.POST.get('type') ,
                'size':  request.POST.get('size'),
            }
            collection.insert_one(pizza)
            return redirect(home)
    collection=mongoCollection('sizes')
    sizes = list(collection.find())
    sizes=[size['size'] for size in sizes]
    return render(request,'pizza/createPizza.html',{'title':'Create Pizza','sizes':sizes})

def deletePizza(request,delete_id):
    collection=mongoCollection('pizzas')
    collection.delete_one({'_id':ObjectId(delete_id)})
    return redirect(home)

def updatePizza(request,update_id):
    collection=mongoCollection('sizes')
    sizes = list(collection.find())
    sizes=[size['size'] for size in sizes]
    collection=mongoCollection('pizzas')
    pizza=collection.find_one({'_id':ObjectId(update_id)})

    if request.method =='POST' :
        if request.POST.get("add_size"):
            addSize(request.POST.get("add_size"))
        else:
            _filter = { '_id': ObjectId(update_id) }
            newvalues = { "$set": { 
                'title': request.POST.get('title') ,
                'description':  request.POST.get('description'), 
                'toppings':  request.POST.get('toppings'),
                'type': request.POST.get('type') ,
                'size':  request.POST.get('size'),
                } 
            }
            collection.update_one(_filter, newvalues) 
            return redirect(home)
    return render(request,'pizza/updatePizza.html',{'title':'Update','sizes':sizes,'pizza':pizza,'id':update_id})

def viewPizza(request,view_id):
    collection=mongoCollection('pizzas')
    pizza=collection.find_one({'_id':ObjectId(view_id)})
    return render(request,'pizza/viewPizza.html',{'title':'Detail','pizza':pizza,'id':view_id})