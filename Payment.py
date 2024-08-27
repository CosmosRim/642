class Payment:
    def __init__(self, customer, Amout,Date):
        self.__customer = customer
        self.__paymentAmout = Amout
        self.__paymentDate = Date
        
    @property
    def customer(self):
        return self.__customer
    
    @customer.setter
    def customer(self, customer):
        self.__customer = customer
    
    @property
    def paymentAmout(self):
        return self.__paymentAmout
    
    @paymentAmout.setter
    def paymentAmout(self, paymentAmout):
        self.__paymentAmout = paymentAmout
        
    @property
    def paymentDate(self):
        return self.__paymentDate
    
    @paymentDate.setter
    def paymentDate(self, paymentDate):
        self.__paymentDate = paymentDate
    
    def display_payment(self):
        print(self.customer, self.paymentAmout, self.paymentDate)
        