class Product:
    # __product_dict = {}
    
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        # Product.__product_dict[name] = self
    
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
        
    # @classmethod
    # def get_price(cls, name):
    #     product = cls.__product_dict.get(name)
    #     return product.price
    
	# set default return value of current class    
    def __str__(self) -> str:
        return f"{self.name}, ${self.price}"