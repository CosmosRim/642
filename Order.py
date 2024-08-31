from datetime import datetime

class Order:
    __nextID = 0
	# start the first customer with ID 1000 and the first order with ID 10000
    __orderID = 10000
    
    def __init__(self, customer):
        self.__customer = customer
		# Payments and orders should be automatically assigned the current date when the objects are created.
        self.__orderdate = datetime.now()
        self.__orderID += Order.__nextID
        Order.__nextID += 1
	
    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer = customer

    @property
    def orderdate(self):
        return self.__orderdate

    @property
    def order_id(self):
        return self.__orderID

    @property
    def nextID(self):
        return self.__orderID + self.__nextID
        
    def display_order(self):
        print(self.customer, self.nextID, self.orderdate, self.orderID)
        
	# set default return value of current class
    def __str__(self) -> str:
        return f"{self.customer}, {self.nextID}, {self.orderdate}, {self.orderID}"
        