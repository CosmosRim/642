class OrderItem:
    __nextID = 0
    __orderItemID = 100000
    
    def __init__(self, orderID, quantity, productName):
        self.__orderItemID += OrderItem.__nextID
        OrderItem.__nextID += 1
        self.__orderID = orderID
        self.__quantity = quantity
        self.__productName = productName
        
    @property
    def order_item_id(self):
        return self.__orderItemID

    @property
    def order_id(self):
        return self.__orderID
    
    @order_id.setter
    def order_id(self, orderID):
        self.__orderID = orderID
    
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
    
    # def add_order_item(self, order_item):
    #     self.items.append(order_item)
        
    def total_price(self):
        return self.__orderID * self.__quantity
    
    def __str__(self) -> str:
        return f"{self.__orderID} * {self.__quantity} = {self.__total_Price}"