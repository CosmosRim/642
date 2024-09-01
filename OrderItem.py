from Product import Product
class OrderItem:
    __nextID = 0
    
    def __init__(self, order, quantity, productName):
        self.__orderID = order.order_id
        self.__orderItemID = order.order_id * 100 + OrderItem.__nextID
        OrderItem.__nextID += 1
        self.__quantity = quantity
        self.__productName = productName
        
    @property
    def order_id(self):
        return self.__orderID
    
    @order_id.setter
    def order_id(self, orderID):
        self.__orderID = orderID
    
    @property
    def order_item_id(self):
        return self.__orderItemID

    @property
    def quantity(self):
        return self.__quantity
        
    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    @property
    def product_name(self):
        return self.__productName
        
    @quantity.setter
    def product_name(self, productName):
        self.__productName = productName
    
	# set default return value of current class
    def __str__(self) -> str:
        return f"{self.order_id}, {self.quantity}, {self.product_name}"