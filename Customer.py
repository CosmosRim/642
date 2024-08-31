class Customer():
    __nextID = 0
	# start the first customer with ID 1000 and the first order with ID 10000
    __customerID = 1000
    
    def __init__(self, balance, name):
        self.__customerBalance = balance
        self.__customerID += Customer.__nextID
        Customer.__nextID += 1
        self.customerName = name
    
    @property
    def customerBalance(self):
        return self.__customerBalance

    @customerBalance.setter
    def customerBalance(self, customerBalance):
        self.__customerBalance = customerBalance

    @property
    def customerID(self):
        return self.__customerID

    @customerID.setter
    def customerID(self, customerID):
        self.__customerID = customerID

    @property
    def customerName(self):
        return self.__customerName

    @customerName.setter
    def customerName(self, customerName):
        self.__customerName = customerName
    
    @property
    def nextID(self):
        return self.__customerID + self.__nextID

    # def add_order(self, order):
    #     self.orders.append(order)
    
    # def add_payment(self, payment):
    #     self.payments.append(payment)

    def add_balance(self, amount):
        self.__customerBalance += amount
        
    def display_customer(self):
        print(self.customerBalance, self.customerID, self.customerName, self.nextID)
        
	# set default return value of current class
    def __str__(self) -> str:
        return f"{self.customerBalance}, {self.customerID}, {self.customerName}, {self.nextID}"