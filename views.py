from lib2to3.pgen2 import driver
from posixpath import split
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
@views.route("/map/")
def map():
    return render_template("map.html")

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/test")
def test():
    return render_template("profile.html")

@views.route("/soloRide/")
def soloRide():
    return render_template("soloRide.html",location=location)
@views.route("/sharedRide/")
def sharedRide(): 
    return render_template("sharedRide.html",location=location)
@views.route("/soloRideResult/")
def soloRideResult():
    print(request.args.get("passenger"))
    print(request.args.get("capacity"))
    print(request.args.get("faddress"))
    print(request.args.get("taddress"))

    customerList = []
    customerStart = Client.search(request.args.get("faddress")).get('results')
    customerstart = next(iter(customerStart))    
    customerEnd = Client.search(request.args.get("taddress")).get('results')
    customerend = next(iter(customerEnd))
    
    print(customerstart.get('LATITUDE'))
    print(customerstart.get('LONGITUDE'))
    print(customerend.get('LATITUDE'))
    print(customerend.get('LONGITUDE'))

    customerList.append(
    mn.Customer(request.args.get("passenger"), int(request.args.get("capacity")),
             (customerstart.get('LATITUDE'), customerstart.get('LONGITUDE')),
             (customerend.get('LATITUDE'), customerend.get('LONGITUDE')),
             False))
    #total capcity <=6
    #list for customer
    #list driver
    #userToDrive(listC,listD)
    print(mn.driverList)
    result = mn.UserToDriver(customerList,mn.driverList)
    print(result)
    key = result.keys()
    for i in key:
        driverName = i
        line =result.get(i)[0]
        point = result.get(i)[1]
        price = result.get(i)[2]
        time = result.get(i)[3]
        distance = result.get(i)[4]
    #return currentMatching
    # drivername [0]-> routeline, [1] -> point [2]-> price [3]->time [4]-> distance [5,n]->customers
    #'Arif': ('[[1.31953153944608,103.674704066438],[1.320388255,103.6764765],[1.319937764,103.6702538],[1.32106717077162,103.672118515084],[1.319937764,103.6702538],[1.317234813,103.6703825],[1.3149609,103.6706185],[1.312021971,103.6707473],[1.312236492,103.667078],[1.309361916,103.6651254],[1.30940312312781,103.664771262225]]:255,0,0:3', '[1.31953153944608,103.674704066438,"255,178,0","A"]|[1.32106717077162,103.672118515084,"255,178,0","B"]|[1.30940312312781,103.664771262225,"255,178,0","C"]'), 
    return render_template("soloRideResult.html", passager=request.args.get("passenger"), capacity=request.args.get("capacity"), faddress=request.args.get("faddress"), taddress=request.args.get("taddress"), driverName=driverName, line=line, point=point, price=price, time=time, distance=distance)
@views.route("/sharedRideResult/")
def sharedRideResult():
    stringLocation = request.args.get("locationsValue")  
    singlePassager = stringLocation.split(";")
    #set can only have 2 set of customer
    #total capcity <=6

    #list for customer
    #list driver
    #userToDrive(listC,listD)
    #return currentMatching
    # drivername [0]-> routeline, [1] -> point [2]-> price [3]->time [4]-> distance [5,n]->customers
    #'Arif': ('[[1.31953153944608,103.674704066438],[1.320388255,103.6764765],[1.319937764,103.6702538],[1.32106717077162,103.672118515084],[1.319937764,103.6702538],[1.317234813,103.6703825],[1.3149609,103.6706185],[1.312021971,103.6707473],[1.312236492,103.667078],[1.309361916,103.6651254],[1.30940312312781,103.664771262225]]:255,0,0:3', '[1.31953153944608,103.674704066438,"255,178,0","A"]|[1.32106717077162,103.672118515084,"255,178,0","B"]|[1.30940312312781,103.664771262225,"255,178,0","C"]'), 
    print("tester"+mn.driverList)
    
    return


#Paramter so the website/user/<variable>
@views.route("/user/<username>")
def user(username):
    return render_template("index.html", name = username)

#Query paramater so the website/profile?name=
@views.route("/profile/")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name = name)

@views.route("/json")
def get_json():
    return jsonify({'name':'example', 'see':'5'})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))