from datetime import datetime

class Order:
    __counter = 0
	# start the first customer with ID 1000 and the first order with ID 10000
    __orderBaseID = 10000
    
    def __init__(self, customerName):
        self.__customerName = customerName
		# Payments and orders should be automatically assigned the current date when the objects are created.
        self.__orderDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.__orderID = self.__orderBaseID + self.__counter
        self.__counter += 1
        self.__nextId = self.__orderBaseID + self.__counter
        self.__status = "uncommit"
        self.__amount = 0
	
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
        return self.__nextId
    
    @property
    def status(self):
        return self.__status
	
    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    def display_order(self):
        print(self.customer_name, self.order_id, self.next_id, self.order_date, self.status, self.amount)
        
	# set default return value of current class
    def __str__(self) -> str:
        return f"{self.customer_name}, {self.order_id}, {self.next_id}, {self.order_date}, {self.status}, {self.amount}"
        