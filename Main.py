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
    
    for cust in controller.customers:
        print(cust)
        
    for prod in controller.products:
        print(prod)
        
    # create fake orders
    cust1 = controller.customers[0]
    prod1 = controller.products[0]
    prod2 = controller.products[1]
    
    # order = Order(cust1, datetime.now())
    # order.add_order_item(prod1, 1)
    # order.add_order_item(prod2, 2)
    # controller.add_order(order)
    
    # for ord in controller.orders:
    #     print(ord)
    
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
    
    # Controller.display_order()
    # Controller.display_payment()
    # Controller.display_order_item()
    # Controller.display_product()
    # Customer.display_customer()
    # Order.display_order()
    # Payment.display_payment()
    # OrderItem.display_order_item()
    # Product.display_product()
    
def load_customers(controller):
    with open("customer.txt", "r") as file:
        for line in file:
            name = line.strip()
            customer = Customer(0, name)
            controller.add_customer(customer)                    
def load_products(controller):
    with open("product.txt", "r") as file:
        for line in file:
            name, price = line.strip().split(",")
            product = Product(name, float(price))
            controller.add_product(product)
    
if __name__ == "__main__":
    main()
        