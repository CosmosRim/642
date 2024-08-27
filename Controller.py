class Controller:
    
    def __init__(self):
        self.__customers = []
        self.__orders = []
        self.__products = []
        self.__payments = []
    
    @property
    def customers(self):
        return self.__customers
    
    @customers.setter
    def customers(self, customers):
        self.__customers = customers

    @property
    def orders(self):
        return self.__orders
    
    @orders.setter
    def orders(self, orders):
        self.__orders = orders

    @property
    def products(self):
        return self.__products
    
    @products.setter
    def products(self, products):
        self.__products = products

    @property
    def payments(self):
        return self.__payments
    
    @payments.setter
    def payments(self, payments):
        self.__payments = payments

# Create and maintain customers, orders, products and payments. 
    def add_customer(self, customer):
        self.__customers.append(customer)
        
    def add_product(self, product):
        self.__products.append(product)
    
    def add_order(self, customer_name,order):
        customer = self.__find_customer(customer_name)
        if customer is not None:
            self.__customer.add_order(order)
            self.__orders.append(order)
            return True
        return False
    
    def add_order_item(self, order, product_name, quantity):
        product = self.__find_product(product_name)
        if product is not None:
            order.add_order_item(product, quantity)
            return True
        return False
    
    def add_payment(self, customer_name, payment):
        customer = self.__find_customer(customer_name)
        if customer is not None:
            self.__customer.add_payment(payment)
            self.__payments.append(payment)
            return True
        return False
# Find a customer object based on customer’s name.
    def find_customer(self, customer_name):
        for customer in self.__customers:
            if customer.customerName == customer_name:
                return customer
        return None
# Find a product object based on product’s name.    
    def find_product(self, product_name):
        for product in self.__products:
            if product.productName == product_name:
                return product
        return None

# Add an order for a given customer. 
    def add_order(self, customer_name, orderdate):
        for order in self.__orders:
            if order.customerName == customer_name and order.orderdate == orderdate:
                return order
        return None
    
# Add an order item for a given order. 
    def add_order_item(self, order, product_name, quantity):
        product = self.__find_product(product_name)
        if product is not None:
            order.add_order_item(product, quantity)
            return True
        return False

# Add a payment for a given customer. 
    def add_payment(self, customer_name, payment):
        customer = self.__find_customer(customer_name)
        if customer is not None:
            self.__customer.add_payment(payment)
            self.__payments.append(payment)
            return True
        return False

# Provide the list of orders for a given customer.
    def list_orders_for_customer(self, customer_name):
        customer = self.__find_customer(customer_name)
        if customer:
            return customer.get_orders()
        return[]

#Provide the list of payments for a given customer     
    def list_payments_for_customer(self, customer_name):
        customer = self.__find_customer(customer_name)
        if customer:    
            return customer.get_payments()
        return[] 

# Provide a list of all customers.
    def list_all_customers(self):
        return self.__customers
# Provide a list of all orders.
    def list_all_orders(self):
        return self.__orders
# Provide a list of all payments.
    def list_all_payments(self):
        return self.__payments
