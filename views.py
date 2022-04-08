from lib2to3.pgen2 import driver
from posixpath import split
from numpy import signedinteger
from onemapsg import OneMapClient
from flask import Blueprint, render_template, request,jsonify, redirect, url_for
import main as mn

Client = OneMapClient("ridhwanproper@gmail.com", "esMrbzVsFr")

views = Blueprint(__name__, "views")

postalCode = ['629215', '629197', '629541', '628509', '629637', '629613']
poi = [
    'GUL CIRCLE MRT STATION (EW30)', 'GUL CIRCLE DISTRICENTRE', 'GUL STREET 2',
    '19 GUL LANE', '126 GUL CIRCLE', '24249 (BUS STOP)', '24229 (BUS STOP)'
]
location = postalCode+poi

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/map/")
def map():
    return render_template("map.html")

@views.route("/soloRide/")
def soloRide():
    return render_template("soloRide.html",location=location)

@views.route("/sharedRide/")
def sharedRide(): 
    return render_template("sharedRide.html",location=location)

@views.route("/soloRideResult/")
def soloRideResult():
    customerList = []
    customerStart = Client.search(request.args.get("faddress")).get('results')
    customerstart = next(iter(customerStart))    
    customerEnd = Client.search(request.args.get("taddress")).get('results')
    customerend = next(iter(customerEnd))

    customerList.append(
    mn.Customer(request.args.get("passenger"), int(request.args.get("capacity")),
             (customerstart.get('LATITUDE'), customerstart.get('LONGITUDE')),
             (customerend.get('LATITUDE'), customerend.get('LONGITUDE')),
             False))

    result = mn.UserToDriver(customerList,mn.driverList)
    key = result.keys()
    for i in key:
        driverName = i
        lines =result.get(i)[0]
        points = result.get(i)[1]
        price = result.get(i)[2]
        time = result.get(i)[3]
        distance = result.get(i)[4]

    return render_template("soloRideResult.html", passenger=request.args.get("passenger"), capacity=request.args.get("capacity"), faddress=request.args.get("faddress"), taddress=request.args.get("taddress"), driverName=driverName, lines=lines, points=points, price=price, time=time, distance=distance)

@views.route("/sharedRideResult/")
def sharedRideResult():
    stringLocation = request.args.get("locationsValue")  
    singlePassager = stringLocation.split(";")
    if(singlePassager[-1]==''):
        singlePassager.remove('')
    customerList = []
    tripList = []
    singletripList = []
    for trip in singlePassager:
        item = trip.split(",")

        singletripList = [item[0], item[1], item[2],item[3]]
        tripList.append(singletripList)

        customerStart = Client.search(item[2]).get('results')
        customerstart = next(iter(customerStart))    
        customerEnd = Client.search(item[3]).get('results')
        customerend = next(iter(customerEnd))

        customerList.append(
        mn.Customer(item[0], int(item[1]),
                (customerstart.get('LATITUDE'), customerstart.get('LONGITUDE')),
                (customerend.get('LATITUDE'), customerend.get('LONGITUDE')),
                True))
    result = mn.UserToDriver(customerList,mn.driverList)
    key = result.keys()
    for i in key:
        driverName = i
        lines =result.get(i)[0]
        points = result.get(i)[1]
        price = result.get(i)[2]
        time = result.get(i)[3]
        distance = result.get(i)[4]

    return render_template("sharedRideResult.html",tripList=tripList,driverName=driverName, lines=lines, points=points, price=price, time=time, distance=distance)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))