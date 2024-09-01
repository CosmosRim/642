from datetime import datetime

class Order:
    __nextID = 0
	# start the first customer with ID 1000 and the first order with ID 10000
    __orderID = 10000
    
    def __init__(self, customerName):
        self.__customerName = customerName
		# Payments and orders should be automatically assigned the current date when the objects are created.
        self.__orderDate = datetime.now()
        self.__orderID += Order.__nextID
        Order.__nextID += 1
	
    @property
    def customer_name(self):
        return self.__customerName

    @customer_name.setter
    def customer(self, customerName):
        self.__customerName = customerName

    @property
    def order_date(self):
        return self.__orderDate

    @property
    def order_id(self):
        return self.__orderID

    @property
    def next_id(self):
        return self.__orderID + self.__nextID
        
    def display_order(self):
        print(self.customer_name, self.next_id, self.order_date, self.order_id)
        
	# set default return value of current class
    def __str__(self) -> str:
        return f"{self.customer_name}, {self.next_id}, {self.order_date}, {self.order_id}"
        