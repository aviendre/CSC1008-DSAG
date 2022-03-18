class Customer:

    def __init__(self, name, capacity, start_point, end_point):
        self.name = name
        self.capacity = capacity
        self.start_point = start_point
        self.end_point = end_point
    
class CustomerSolo(Customer):

    def __init__(self, name, capacity, start_point, end_point):
        super().__init__(name, capacity, start_point, end_point)

class CustomerShared(Customer):

    def __init__(self, name, capacity, start_point, end_point):
        super().__init__(name, capacity, start_point, end_point)

