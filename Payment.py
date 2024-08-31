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
    def payment_amount(self):
        return self.__paymentAmount
    
    @payment_amount.setter
    def payment_amount(self, paymentAmount):
        self.__paymentAmount = paymentAmount
        
    @property
    def payment_date(self):
        return self.__paymentDate
    
    @payment_date.setter
    def paymentDate(self, paymentDate):
        self.__paymentDate = paymentDate
    
    @property
    def current_date(self):
        return self.__currentDate

    def display_payment(self):
        print(self.customer, self.paymentAmount, self.paymentDate)
	
	# set default return value of current class
    def __str__(self) -> str:
        return f"{self.customer}, {self.payment_amount}, {self.payment_date}"
        