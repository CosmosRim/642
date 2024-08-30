from Controller import Controller  
from Customer import Customer
from Order import Order
from Payment import Payment
from OrderItem import OrderItem
from Product import Product
from datetime import datetime

def main():
    controller = Controller()

    # Display a given customer’s information.
    def get_customer_info(self, name):
        customer = self.find_customer_by_name(name)
        if customer:
            return f"Customer ID: {customer.customer_id}\nName: {customer.name}\nEmail: {customer.email}\nBalance: ${customer.balance:.2f}"
        else:
            return "Customer not found."

    # Create and process orders for existing customers.
    def create_order(self, customer_name):
        customer = self.find_customer_by_name(customer_name)
        if customer:
            order = Order(customer)
            self._orders.append(order)
            customer.add_order(order)
            return order
        else:
            raise ValueError("Customer not found.")
    
    def add_order_item(self, order, product_name, quantity):
        product = self.find_product_by_name(product_name)
        if product:
            order_item = OrderItem(product, quantity)
            order.add_order_item(order_item)
        else:
            raise ValueError("Product not found.")
        
    def process_order(self, order):
        total_amount = order.calculate_total()
        order.customer.update_balance(total_amount)
        order.complete_order()

    # Accept payments from customers.
    def add_payment(self, customer_name, Amount):
        customer = self.find_customer_by_name(customer_name)
        if customer:
            payment = Payment(customer, Amount)
            self._payments.append(payment)
            customer.update_balance(- Amount)  # Subtract payment from balance
        else:
            raise ValueError("Customer not found.")

    # List all orders for a given customer.
    def get_orders_for_customer(self, customer_name):
        customer = self.find_customer_by_name(customer_name)
        if customer:
            if customer.orders:
                orders_list = []
                for order in customer.orders:
                    order_info = f"Order ID: {order.order_id}, Date: {order.date.strftime('%Y-%m-%d')}, Total: ${order.calculate_total():.2f}"
                    orders_list.append(order_info)
                return "\n".join(orders_list)
            else:
                return "No orders found for this customer."
        else:
            return "Customer not found."

    # List all payments from a given customer.
    def get_payments_for_customer(self, customer_name):
        customer = self.find_customer_by_name(customer_name)
        if customer:
            if customer.payments:
                payments_list = []
                for payment in customer.payments:
                    payment_info = f"Payment ID: {payment.payment_id}, Date: {payment.date.strftime('%Y-%m-%d')}, Amount: ${payment.amount:.2f}"
                    payments_list.append(payment_info)
                return "\n".join(payments_list)
            else:
                return "No payments found for this customer."
        else:
            return "Customer not found."

    # List all customers.
    for cust in controller.customers:
        print(cust)

    # List all orders.
    for order in controller.orders:
        print(order)
            
    # List all payments.
    for pay in controller.payments:
        print(pay)

    # Read the supplied files and create the appropriate customer and product objects. This information must be made visible to the user.
    def load_customers(controller):
        with open("customer.txt", "r") as file:
            for line in file:
                name = line.strip()
                customer = Customer(0, name)
                controller.add_customer(customer)                    

    # Create a new order for a selected customer.
    def find_customer_by_name(self, name):
        for customer in self.customers:
            if customer.name == name:
                return customer
        return None

    def find_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    # Add products and quantities (as order items) to the order. Current total of the order must be visible to the user.
    def load_products(controller):
        with open("product.txt", "r") as file:
            for line in file:
                name, price = line.strip().split(",")
                product = Product(name, float(price))
                controller.add_product(product)
    
    # Load customers and products from files
    load_customers(controller)
    load_products(controller)

    for prod in controller.products:
        print(prod)

    prod1 = controller.products[0]
    prod2 = controller.products[1]

    # Completed order must be submitted and the customer’s balance must be updated.
    def submit_order(self, order):
        if order in self._orders:
            total_cost = order.finalize_order()
            return f"Order ID {order.order_id} submitted. Total cost: ${total_cost:.2f}. Customer's new balance: ${order.customer.balance:.2f}"
        else:
            return "Order not found."
        
    # Make a payment for a selected customer. Customer’s balance must be updated to reflect this payment.
    def add_payment(self, customer_name, amount):
        customer = self.find_customer_by_name(customer_name)
        if customer and amount > 0:
            payment = Payment(amount, customer)
            customer.add_payment(payment)
            self._payments.append(payment)
            return f"Payment of ${amount:.2f} received from {customer_name}. New balance: ${customer.balance:.2f}"
        else:
            raise ValueError("Invalid customer or amount")

    # Display the list of orders for a selected customer.
    def get_orders_for_customer(self, customer_name):
        customer = self.find_customer_by_name(customer_name)
        if customer:
            return customer.orders
        else:
            raise ValueError("Customer not found")

    # Display the list of payments for a selected customer.
    def get_payments_for_customer(self, customer_name):
        customer = self.find_customer_by_name(customer_name)
        if customer:
            return customer.payments
        else:
            raise ValueError("Customer not found")

    # Display the list of all customers for the company.
    def get_all_customers(self):
        return self.customers

    # Display the list of all the orders for the company.
    def get_all_orders(self):
        return self._orders
    
    # Display the list of all payments for the company.
    def get_all_payments(self):
        return self._payments

    # Have a user interface with the appropriate user controls, useful feedback, and prevention of input errors.TKinter使用的


    # while True:
    #  print("\n--- Main Menu ---")
    #  print("1. List All Customers")
    #  print("8. List All Payments")
    #  print("9. Exit")

if __name__ == "__main__":
    main()
        