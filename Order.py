from datetime import datetime
from Customer import Customer

class Order:
    __nextID = 0
    __orderID = 10000
    
    def __init__(self, customer, orderdate):
        self.__customer = customer
        self.__orderdate = orderdate
        self.__orderID += Order.__nextID
        Order.__nextID += 1
        self.__currentdate = datetime.now()
	
    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer = customer

    @property
    def orderdate(self):
        return self.__orderdate

    @orderdate.setter
    def orderdate(self, orderdate):
        self.__orderdate = orderdate

    @property
    def nextID(self):
        return self.__nextID

    @nextID.setter
    def nextID(self, value):
        self.__nextID = value
	
    @property
    def currentdate(self):
        return self.__currentdate
        
    def display_order(self):
        print(self.customer, self.nextID, self.orderdate, self.orderID)
    
    def finalize_order(self):
        total_cost = self.calculate_total()
        self.customer.balance += total_cost
        return total_cost
        
    def __str__(self) -> str:
        return f"{self.customer}, {self.nextID}, {self.orderdate}, {self.orderID}"
        