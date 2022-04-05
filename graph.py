# -----------------------------------
# Retrieves all the data from the csv
# file and creates a list
# -----------------------------------

import pandas,csv
from math import sin, cos, sqrt, asin, radians

RADIUS = 6371

def calculateDist(lat1,lon1,lat2,lon2):
    #Haversine Formula
    R = 6372.8 # this is in miles.  For Earth radius in kilometers use 6372.8 km

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))

    return R * c

def GraphNode():
    x = 1
    intersection = []
    intersection_list = pandas.read_csv('points.csv')
    for i in intersection_list['Intersection']:
        intersection.append(i)

    data_lat_long = pandas.read_csv('points.csv')
    dict_lat_lng = data_lat_long.to_dict()
    points = {}
    for i in range(len(intersection)):
        points[dict_lat_lng['Intersection'][i]] = (dict_lat_lng['Longitude'][i],dict_lat_lng['Latitude'][i],dict_lat_lng['Connected'][i])
    return points