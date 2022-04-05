from os import link
import queue
import LinkedList

class driver(object):
    def __init__(self,name,currentLocation,capacity):
        self.name = name
        self.currentLocation = currentLocation
        self.capacity = capacity

class soloDriver(driver):
    def __init__(self, name, currentLocation, capacity):
        super().__init__(name, currentLocation, capacity)
        self.endpoint = queue.Queue() 
        self.customer = []

    def addNewRoute():
        pass

    def removeRoute():
        pass

class sharedDriver(driver):
    def __init__(self, name, currentLocation, capacity):
        super().__init__(name, currentLocation, capacity)
        self.customer = []
        self.endpoint = LinkedList.LinkedList()

