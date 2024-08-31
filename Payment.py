from datetime import datetime
class Payment:
    def __init__(self, customer, amount, date):
        self.__customer = customer
        self.__paymentAmount = amount
        self.__paymentDate = date
        self.__currentDate = datetime.now()
        
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
    
    @property
    def currentDate(self):
        return self.__currentDate

    def display_payment(self):
        print(self.customer, self.paymentAmount, self.paymentDate)
	
    def __str__(self) -> str:
        return f"{self.customer}, {self.paymentAmount}, {self.paymentDate}"
        