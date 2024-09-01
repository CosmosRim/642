class Customer():
    __nextID = 0
	# start the first customer with ID 1000 and the first order with ID 10000
    __customerID = 1000
    
    def __init__(self, balance, name):
        self.__customerBalance = balance
        self.__customerID += Customer.__nextID
        Customer.__nextID += 1
        self.__customerName = name
    
    @property
    def customer_balance(self):
        return self.__customerBalance

    @customer_balance.setter
    def customerBalance(self, customerBalance):
        self.__customerBalance = customerBalance

    @property
    def customer_id(self):
        return self.__customerID

    @property
    def customer_name(self):
        return self.__customerName

    @customer_name.setter
    def customer_name(self, customerName):
        self.__customerName = customerName
    
    @property
    def next_id(self):
        return self.__customerID + self.__nextID
        
    def display_customer(self):
        print(self.customer_balance, self.customer_id, self.customer_name, self.next_id)
        
	# set default return value of current class
    def __str__(self) -> str:
        return f"{self.customer_balance}, {self.customer_id}, {self.customer_name}, {self.next_id}"