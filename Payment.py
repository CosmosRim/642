from datetime import datetime
class Payment:
    def __init__(self, customerName, amount):
        self.__customerName = customerName
        self.__paymentAmount = amount
		# Payments and orders should be automatically assigned the current date when the objects are created.
        self.__paymentDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
    @property
    def customer_name(self):
        return self.__customerName
    
    @customer_name.setter
    def customer(self, customerName):
        self.__customerName = customerName
    
    @property
    def payment_amount(self):
        return self.__paymentAmount
    
    @payment_amount.setter
    def payment_amount(self, paymentAmount):
        self.__paymentAmount = paymentAmount
        
    @property
    def payment_date(self):
        return self.__paymentDate

    def display_payment(self):
        print(self.customer, self.paymentAmount, self.paymentDate)
	
	# set default return value of current class
    def __str__(self) -> str:
        # return f"{self.customer}, {self.payment_amount}, {self.payment_date}"
        return f"Customer Name: {self.customer}, Payment Amount: {self.payment_amount}, Payment Date: {self.payment_date}"
        