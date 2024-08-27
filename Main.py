from Controller import Controller  
from Customer import Customer
from Order import Order
from Payment import Payment
from OrderItem import OrderItem
from Product import Product
from datetime import datetime

def main():
    controller = Controller()

    # Load customers and products from files
    load_customers(controller)
    load_products(controller)
    
    for prod in controller.products:
        print(prod)
        
    # create fake orders
    cust1 = controller.customers[0]
    prod1 = controller.products[0]
    prod2 = controller.products[1]
    
    # Display a given customer’s information.
    
    # Create and process orders for existing customers.
    
    # Accept payments from customers.
    
    # List all orders for a given customer.
    
    # List all payments from a given customer.
    
    # List all customers.
    for cust in controller.customers:
        print(cust)
    
    # List all orders.
    
    # List all payments.
    
    
    
    # Read the supplied files and create the appropriate customer and product objects. This information must be made visible to the user.
    def load_customers(controller):
        with open("customer.txt", "r") as file:
            for line in file:
                name = line.strip()
                customer = Customer(0, name)
                controller.add_customer(customer)                    
    
    # Create a new order for a selected customer.
    
    # Add products and quantities (as order items) to the order. Current total of the order must be visible to the user.
    def load_products(controller):
        with open("product.txt", "r") as file:
            for line in file:
                name, price = line.strip().split(",")
                product = Product(name, float(price))
                controller.add_product(product)
        
    # Completed order must be submitted and the customer’s balance must be updated.
    
    # Make a payment for a selected customer. Customer’s balance must be updated to reflect this payment.
    
    # Display the list of orders for a selected customer.
    
    # Display the list of payments for a selected customer.
	
    # Display the list of all customers for the company.

    # Display the list of all the orders for the company.

    # Display the list of all payments for the company.

    # Have a user interface with the appropriate user controls, useful feedback, and prevention of input errors.


    # while True:
    #  print("\n--- Main Menu ---")
    #  print("1. List All Customers")
    #  print("2. Create New Order")
    #  print("3. Add Order Item")
    #  print("4. Make Payment")
    #  print("5. List Orders for Customer")
    #  print("6. List Payments for Customer")
    #  print("7. List All Orders")
    #  print("8. List All Payments")
    #  print("9. Exit")
    
if __name__ == "__main__":
    main()
