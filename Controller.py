from Order import Order
from Customer import Customer
from Order import Order
from OrderItem import OrderItem
from Product import Product
from Payment import Payment

class Controller:
    
    def __init__(self):
        self.__customers = {}
        self.__orders = []
        self.__orderItems = []
        self.__products = {}
        self.__payments = []

    # Create and maintain customers, orders, products and payments. 
    def add_customer(self, customer):
        self.__customers[customer.customer_name] = customer
        
    def add_product(self, product):
        self.__products[product.product_name] = product
    
    # Add an order for a given customer. 
	# b. Create a new order for a selected customer.
    def add_order(self, customer, order):
        customer = self.find_customer(customer.customer_name)
        if customer is not None:
            self.__orders.append(order)
            return True
        return False
    
    # Add an order item for a given order.
    # c. Add products and quantities (as order items) to the order
    def add_order_item(self, productName, orderItem):
        product = self.find_product(productName)
        if product is not None:
            self.__orderItems.append(orderItem)
            return True
        return False
    
    # Add a payment for a given customer. 
    def add_payment(self, customer_name, payment):
        customer = self.find_customer(customer_name)
        if customer is not None:
            self.__payments.append(payment)
            return True
        return False
    
    # Find a customer object based on customer’s name.
    def find_customer(self, customer_name):
        return self.__customers.get(customer_name)

    # Find a product object based on product’s name.    
    def find_product(self, product_name):
        return self.__products.get(product_name)

    # Provide the list of orders for a given customer.
	# f. Display the list of orders for a selected customer.
    def list_orders_for_customer(self, customer_name):
        customer = self.find_customer(customer_name)
        if customer:
            return customer.get_orders()
        return[]

    # Provide the list of payments for a given customer     
    # g. Display the list of payments for a selected customer.
    def list_payments_for_customer(self, customer_name):
        for payment in self.__payments:
            if customer_name == payment.customer:    
                return payment
        return None

    # Provide a list of all customers.
    def list_all_customers(self):
        return self.__customers

    # Provide a list of all orders.
    def list_all_orders(self):
        return self.__orders

    # Provide a list of all payments.
    def list_all_payments(self):
        return self.__payments

    # a. Read the supplied files and create the appropriate customer and product objects.
    with open("customer.txt", "r") as file:
        for line in file:
            name = line.strip()
            customer = Customer(0, name)
            add_customer(customer) 

    with open("product.txt", "r") as file:
        for line in file:
            name, price = line.strip().split(",")
            product = Product(name, float(price))
            add_product(product)
    
    # d. Completed order must be submitted and the customer’s balance must be updated.

	# e. Make a payment for a selected customer. Customer’s balance must be updated to reflect this payment.

    # h. Display the list of all customers for the company.
    for cust in self.__customers:
        print(cust)

    # i. Display the list of all the orders for the company.
    for order in self.__orders:
        print(order)

    # j. Display the list of all payments for the company.
    for pay in self.payments:
        print(pay)

    # k. Have a user interface with the appropriate user controls, useful feedback, and prevention of input errors.