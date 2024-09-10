
import customtkinter as ctk
import Controller

# set default theme and colour
ctk.set_appearance_mode("System")  # set default theme follow system, there are "Light", "Dark" and "System" in total.
ctk.set_default_color_theme("blue")  # set default colour to blue.

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # set window title and size
        self.title("Order Management System")
        self.geometry("1200x800")

        # make window size changable
        self.grid_columnconfigure(1, weight=1)  # middle frame support column extend
        self.grid_rowconfigure(0, weight=1)     # all lines support row extend

        # left zone buttons
        left_frame = ctk.CTkFrame(self)
        left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")
		
        # make row 4 extandable, to put row 5 to 7 to buttom
        left_frame.grid_rowconfigure(4, weight=1)
        left_frame.grid_rowconfigure(6, weight=1)
        
        # left zone buttons
        self.show_payments_btn = ctk.CTkButton(left_frame, text="Show All Prodcutions", command=self.show_all_prod)
        self.show_payments_btn.grid(row=0, column=0, pady=10)
        
        self.show_customers_btn = ctk.CTkButton(left_frame, text="Show All Customers", command=self.show_all_customers)
        self.show_customers_btn.grid(row=1, column=0, pady=10)

        self.show_payments_btn = ctk.CTkButton(left_frame, text="Show All Payments", command=self.show_all_payments)
        self.show_payments_btn.grid(row=2, column=0, pady=10)

        self.show_orders_btn = ctk.CTkButton(left_frame, text="Show All Orders", command=self.show_all_orders)
        self.show_orders_btn.grid(row=3, column=0, pady=10)

        self.show_orders_btn = ctk.CTkButton(left_frame, text="Clean All Messages", command=self.clean_inputs)
        self.show_orders_btn.grid(row=5, column=0, pady=10)

        # Appearance support change 
        appearance_mode_label = ctk.CTkLabel(left_frame, text="Appearance Mode:")
        appearance_mode_label.grid(row=7, column=0, padx=20, pady=5, sticky="w")

        self.appearance_mode_optionmenu = ctk.CTkOptionMenu(left_frame, values=["Light", "Dark", "System"],
                                                            command=self.change_appearance_mode)
        self.appearance_mode_optionmenu.grid(row=8, column=0, padx=20, pady=10)
        self.appearance_mode_optionmenu.set("System")  # set default value follow system appearance

        self.exit_btn = ctk.CTkButton(left_frame, text="Exit", command=self.quit)
        self.exit_btn.grid(row=9, column=0, pady=10, sticky="s")

        # Middle zone: Display text box, dropdown menu for selecting Customer, input box for payment amount, and submit button
        middle_frame = ctk.CTkFrame(self)
        middle_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")  # 中间区域可以随窗口扩展

        # Allow control extensions within middle_frame
        middle_frame.grid_columnconfigure(0, weight=2)
        middle_frame.grid_columnconfigure(1, weight=1)
        middle_frame.grid_columnconfigure(2, weight=1)
        middle_frame.grid_rowconfigure(0, weight=1)

        self.textbox = ctk.CTkTextbox(middle_frame, height=300, width=400)
        self.textbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")  # textbox support four directions extend 

        ctk.CTkLabel(middle_frame, text="Select Customer:").grid(row=1, column=0, padx=6, pady=5, sticky="w")
        self.customer_combobox = ctk.CTkComboBox(middle_frame, values=controller.list_all_customers_name(), command=self.on_customer_selected)
        self.customer_combobox.grid(row=2, column=0, padx=6, pady=5, sticky="ew")  # 下拉框随窗口扩展

        self.list_customer_order = ctk.CTkButton(middle_frame, text="Show Cust Order", command=self.show_customer_order)
        self.list_customer_order.grid(row=3, column=0, padx=3, pady=5, sticky="w")

        self.list_customer_pay = ctk.CTkButton(middle_frame, text="Show Cust Pay", command=self.show_customer_pay)
        self.list_customer_pay.grid(row=3, column=0, padx=3, pady=5, sticky="e")

        ctk.CTkLabel(middle_frame, text="Payment Amount:").grid(row=1, column=2, padx=2, pady=5, sticky="w")
		# register python input as a value for tkinter to use, at each time when input any new character
        vcmd = (self.register(self.validate_input_money), '%P')
        self.payment_scale = ctk.CTkEntry(middle_frame, validate="key", validatecommand=vcmd)
        self.payment_scale.grid(row=2, column=2, padx=2, pady=5, sticky="w")

        self.add_payment = ctk.CTkButton(middle_frame, text="Commit", command=self.add_payment)
        self.add_payment.grid(row=3, column=2, padx=2, pady=5, sticky="w")

        # right zone, add order and order items
        right_frame = ctk.CTkFrame(self)
        right_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ns")

        ctk.CTkLabel(right_frame, text="New Orders").grid(row=0, column=0, padx=10, pady=10)
        self.switch1 = ctk.CTkSwitch(right_frame, text="Add New Order", command=self.switch_callback)
        self.switch1.grid(row=1, column=0, padx=10, pady=5, sticky="we")

        ctk.CTkLabel(right_frame, text="Select Product:").grid(row=2, column=0, padx=6, pady=5, sticky="w")
        self.prod_combobox = ctk.CTkComboBox(right_frame, values=controller.list_all_products_name())
        self.prod_combobox.grid(row=3, column=0, padx=6, pady=5, sticky="ew")

        ctk.CTkLabel(right_frame, text="Product Number:").grid(row=4, column=0, padx=2, pady=5, sticky="w")
		# register python input as a value for tkinter to use, at each time when input any new character
        vcmd = (self.register(self.validate_input_number), '%P')
        self.prodcut_num = ctk.CTkEntry(right_frame, validate="key", validatecommand=vcmd)
        self.prodcut_num.grid(row=5, column=0, padx=2, pady=5, sticky="w")

        self.add_payment = ctk.CTkButton(right_frame, text="Add Product to OrderItem", command=self.add_order_item)
        self.add_payment.grid(row=6, column=0, padx=2, pady=5, sticky="w")

        self.add_payment = ctk.CTkButton(right_frame, text="Commit Order", command=self.commit_order)
        self.add_payment.grid(row=7, column=0, padx=2, pady=5, sticky="w")
    
    #Clear Button function
    def clean_inputs(self):
        self.textbox.delete("1.0", "end") # clean all message before insert
        self.textbox.insert("end", "All message are cleanned\n")

    # function for button command
    def show_all_prod(self):
        self.textbox.delete("1.0", "end") # clean all message before insert
        self.textbox.insert("end", "Showing all prodcutions...\n")
        for prod in controller.list_all_products():
            self.textbox.insert("end", f"{prod}\n")
    
    def show_all_customers(self):
        self.textbox.delete("1.0", "end") # clean all message before insert
        self.textbox.insert("end", "Showing all customers...\n")
        for cust in controller.list_all_customers():
            self.textbox.insert("end", f"{cust}\n")

    def show_all_payments(self):
        self.textbox.delete("1.0", "end") # clean all message before insert
        self.textbox.insert("end", "Showing all payments...\n")
        for pay in controller.list_all_payments():
            self.textbox.insert("end", f"{pay}\n")

    def show_all_orders(self):
        self.textbox.delete("1.0", "end") # clean all message before insert
        self.textbox.insert("end", "Showing all orders...\n")
        for order in controller.list_all_orders():
            self.textbox.insert("end", f"{order}\n")

    def add_payment(self):
        cust_name = self.customer_combobox.get()
        payment_value = self.payment_scale.get()
        self.on_customer_selected(cust_name)
        if payment_value == "":
            self.textbox.insert("end", "\nPlease input payment amount")
        else:
            customer = controller.customers[cust_name]
            payment_value = float(payment_value)
            payment = Controller.Payment(cust_name, payment_value)
            balance = customer.customer_balance
            controller.add_payment(customer, payment)
            self.textbox.insert("end", "\nPayment added...\n")
            self.textbox.insert("end", f"${payment_value} already charged into {cust_name}'s balance.\
                \nbefore balance is : {balance}\
                \nnow balance is : {customer.customer_balance}\n")

    def show_customer_order(self):
        cust_name = self.customer_combobox.get()
        self.on_customer_selected(cust_name)
        cust_orers = controller.list_orders_for_customer(cust_name)
        if cust_name is None:
            self.textbox.insert("end", "\nPlease select a customer")
        elif not cust_orers:
            self.textbox.insert("end", f"\n{cust_name} has no order yet\n")
        else:
            self.textbox.insert("end", f"\nShowing customer's order...\n")
            for cust_order in cust_orers:
                self.textbox.insert("end", f"{cust_order}\n")
	
    def show_customer_pay(self):
        cust_name = self.customer_combobox.get()
        self.on_customer_selected(cust_name)
        cust_pays = controller.list_payments_for_customer(cust_name)
        if cust_name is None:
            self.textbox.insert("end", "\nPlease select a customer")
        elif not cust_pays:
            self.textbox.insert("end", f"\n{cust_name} has no payment yet\n")
        else:
            self.textbox.insert("end", f"\nShowing customer's payment...\n")
            for cust_pay in cust_pays:
                self.textbox.insert("end", f"{cust_pay}\n")
	
    def change_appearance_mode(self, new_mode):
        ctk.set_appearance_mode(new_mode)
	
    def on_customer_selected(self, selected_value):
        cust_info = controller.find_customer(selected_value)
        self.textbox.delete("1.0", "end") # clean all message before insert
        self.textbox.insert("end", f"Customer Info:\n{cust_info}\n")

    def validate_input_money(self, new_value):
        if new_value == "" or new_value.isdigit() or (new_value.count('.') == 1 and new_value.replace('.', '').isdigit()):
            return True
        else:
            return False

    # quantity only allow input intger larger than 0
    def validate_input_number(self, new_value):
        if new_value == "":
            return True
        elif new_value.isdigit() and int(new_value) > 0:
            return True
        else:
            return False
	
    def switch_callback(self):
        if self.switch1.get() == 1:
            self.on_switch_on()
        else:
            self.on_switch_off()
	
    def on_switch_on(self):
        cust_name = self.customer_combobox.get()
        self.on_customer_selected(cust_name)
        order = Controller.Order(cust_name)
        controller.add_order(order)
        self.textbox.insert("end", f"\nAdding order\n{order}")
	
	# cancel current order meet some issue, comment now. But fn will remaining, in case void fn calling in other place.
    def on_switch_off(self):
        # cust_name = self.customer_combobox.get()
        # self.on_customer_selected(cust_name)
        # controller.delete_order()
        # self.textbox.insert("end", f"\nDeleting order\n")
        return True

    def add_order_item(self):
        cust_name = self.customer_combobox.get()
        order = Controller.Order(cust_name)
        quantity = self.prodcut_num.get()
        prodcut_name = self.prod_combobox.get()
        product = controller.products[prodcut_name]
        if quantity == "":
            self.textbox.insert("end", "\nPlease input product number, min number is 1")
        else:
            quantity = int(quantity) 
            orderItem = Controller.OrderItem(order, quantity, product)
            controller.add_order_item(orderItem)
            self.textbox.insert("end", f"\n{quantity} of {prodcut_name} as already added to OrderItem")

    def commit_order(self):
        cust_name = self.customer_combobox.get()
        customer = controller.customers[cust_name]
        order = controller.orders[-1]
        controller.commit_order(customer, order)
        self.textbox.insert("end", "\nOrder commited, please check in customer info")
        
        

# __main__ 
if __name__ == "__main__":
    # create a instance for all info
    controller = Controller.Controller()
    # instance call load txt info function from controller
    controller.load_from_files()
    app = App()
    app.mainloop()