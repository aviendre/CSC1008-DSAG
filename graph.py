# -----------------------------------
# Retrieves all the data from the csv
# file and creates a list
# -----------------------------------

import csv
from math import sin, cos, sqrt, atan2, radians

RADIUS = 6371
node = []

def GraphNode():
    '''Read the CSV file and returns to global environment node'''
    global node
    temp = []
    nodeFile = open('points.csv')
    header = []
    header = next(nodeFile)
    for n in nodeFile:
        temp.append(n)
    nodeFile.close()
    for x in temp:
        node.append(str(x).split(','))
    print('\n'.join(map(str,node)))
    #print('\n'.join(map(str,node)))

def Graph():
    pass 

def calculateDist(pointx, pointy):
    #Haversine Formula
    lat1 = radians(pointx.lat)
    lng1 = radians(pointx.lng)
    lat2 = radians(pointy.lat)
    lng2 = radians(pointy.lng)

    dLon = lng2 - lng1
    dLat = lat2 - lat1

    a = sin(dLat / 2)**2 + cos(lat1) * cos(lat2) * sin(dLon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a)) 
    distance = RADIUS * c

    return distance

GraphNode()