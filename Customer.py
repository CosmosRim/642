class Customer():
    __nextID = 0
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
        return self.__nextID

    @nextID.setter
    def nextID(self, value):
        self.__nextID = value
    
    def add_order(self, order):
        self.orders.append(order)
    
    def add_payment(self, payment):
        self.payments.append(payment)

    def update_balance(self, amount):
        self.balance += amount
        
    def display_customer(self):
        print(self.customerBalance, self.customerID, self.customerName, self.nextID)
        
	# set default value of current class
    def __str__(self):
        return f"{self.customerBalance}, {self.customerID}, {self.customerName}, {self.nextID}"