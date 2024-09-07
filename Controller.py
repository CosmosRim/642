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
    def order_items(self):
        return self.__orders

    @order_items.setter
    def order_items(self, orders):
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
        self.__customers[customer.customer_name] = customer
        
    def add_product(self, product):
        self.__products[product.name] = product
    
    # Add an order for a given customer. 
    def add_order(self, order):
        customer = self.find_customer(order.customer_name)
        if customer is not None:
            self.__orders.append(order)
            return True
        return False
    
    # Add an order item for a given order.
    def add_order_item(self, orderItem):
        product = self.find_product(orderItem.product_name)
        if product is not None:
            self.__orderItems.append(orderItem)
            return True
        return False
    
    # Add a payment for a given customer. 
    def add_payment(self, customer, payment):
        customer = self.find_customer(customer.customer_name)
        if customer is not None:
            self.__payments.append(payment)
            self.update_customer_balance(customer, payment.payment_amount)
            return True
        return False
    
    # Find a customer object based on customer’s name.
    def find_customer(self, customer_name):
        return self.__customers.get(customer_name)

    # Find a product object based on product’s name.    
    def find_product(self, product_name):
        return self.__products.get(product_name)

    # Provide the list of orders for a given customer.
    def list_orders_for_customer(self, customer_name):
        orders_for_custoemr = []
        for order in self.__orders:
            if customer_name == order.customer_name:
                orders_for_custoemr.append(order)
        return orders_for_custoemr

    # Provide the list of payments for a given customer     
    def list_payments_for_customer(self, customer_name):
        payments_for_customer = []
        for payment in self.__payments:
            if customer_name == payment.customer_name:
                payments_for_customer.append(payment)
        return payments_for_customer

    # Provide a list of all customers.
    def list_all_customers(self):
        return list(self.__customers.values())

    # Provide a list of all orders.
    def list_all_orders(self):
        return self.__orders

    # Provide a list of all payments.
    def list_all_payments(self):
        return self.__payments
    
    # update customer balance
    def update_customer_balance(self, customer, amount):
        return customer.adjust_balance(amount)
    
    # commit order
    def commit_order(self, customer, order):
        amount = 0
        for orderItem in self.__orderItems:
            if orderItem.order_id == order.order_id:
                amount += orderItem.quantity * orderItem.product_price
        order.status = "commited"
        order.amount = amount
        self.update_customer_balance(customer, -amount)


def main():
    # create a instance for all info
    controller = Controller()
    
    # a. Read the supplied files and create the appropriate customer and product objects.
    with open("customer.txt", "r") as file:
        for line in file:
            name = line.strip()
            customer = Customer(0, name)
            controller.add_customer(customer) 
    
    with open("product.txt", "r") as file:
        for line in file:
            name, price = line.strip().split(",")
            product = Product(name, float(price))
            controller.add_product(product)
    
    # b. Create a new order for a selected customer.
    order = Order("Ignacia Craft")
    controller.add_order(order)
    
    # c. Add products and quantities (as order items) to the order
    orderItem = OrderItem(order, 2, controller.products["Post-it Notes"])
    controller.add_order_item(orderItem)
    
    # d. Completed order must be submitted and the customer’s balance must be updated.
    controller.commit_order(controller.customers["Ignacia Craft"], order)
    
    # e. Make a payment for a selected customer. Customer’s balance must be updated to reflect this payment.
    payment = Payment("Ignacia Craft", 123)
    controller.add_payment(controller.customers["Ignacia Craft"], payment)
    
    print("Orders for Ignacia")
    # f. Display the list of orders for a selected customer.
    for order in controller.list_orders_for_customer("Ignacia Craft"):
        print(order)
    
    print("Payments for Ignacia")
    # g. Display the list of payments for a selected customer.
    for payment in controller.list_payments_for_customer("Ignacia Craft"):
        print(payment)
    
    print("All customer")
    # h. Display the list of all customers for the company.
    for customer in controller.list_all_customers():
        print(customer)
    
    print("All order")
    # i. Display the list of all the orders for the company.
    for order in controller.list_all_orders():
        print(order)
    
    print("All payment")
    # j. Display the list of all payments for the company.
    for payment in controller.list_all_payments():
        print(payment)
    
    # k. Have a user interface with the appropriate user controls, useful feedback, and prevention of input errors.

if __name__ == "__main__":
    main()