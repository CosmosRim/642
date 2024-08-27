class OrderItem:
    def __init__(self, order, quantity):
        self.__order = order
        self.__quantity = quantity
        
    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self, order):
        self.__order = order
    
    @property
    def quantity(self):
        return self.__quantity
        
    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity
        
    def total_price(self):
        return self.__order * self.__quantity
    
    def __str__(self):
        return f"{self.__order} * {self.__quantity} = {self.__total_Price}"