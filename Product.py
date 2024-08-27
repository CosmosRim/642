class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def name(self):
        return self.__name

    def price(self):
        return self.__price
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price
        
    def __str__(self):
        return f"{self.__name}, ${self.__price}"