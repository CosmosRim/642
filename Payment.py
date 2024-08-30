from datetime import datetime
class Payment:
    def __init__(self, customer, Amount,Date):
        self.__customer = customer
        self.__paymentAmount = Amount
        self.__paymentDate = datetime.now()
        
    @property
    def customer(self):
        return self.__customer
    
    @customer.setter
    def customer(self, customer):
        self.__customer = customer
    
    @property
    def paymentAmount(self):
        return self.__paymentAmount
    
    @paymentAmount.setter
    def paymentAmount(self, paymentAmount):
        self.__paymentAmount = paymentAmount
        
    @property
    def paymentDate(self):
        return self.__paymentDate
    
    @paymentDate.setter
    def paymentDate(self, paymentDate):
        self.__paymentDate = paymentDate
    
    def display_payment(self):
        print(self.customer, self.paymentAmount, self.paymentDate)
        