# using a secondary developed tkinter project for better button and layout
# project: https://github.com/TomSchimansky/CustomTkinter
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

        # 允许窗口内容随大小变化
        self.grid_columnconfigure(1, weight=1)  # 中间部分的列扩展
        self.grid_rowconfigure(0, weight=1)     # 所有行可以垂直扩展

        # 左侧区域的按钮
        left_frame = ctk.CTkFrame(self)
        left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")
		
        # make row 4 extandable, to put row 5 to 7 to buttom
        left_frame.grid_rowconfigure(4, weight=1)

        self.show_payments_btn = ctk.CTkButton(left_frame, text="Show All Prodcutions", command=self.show_all_prod)
        self.show_payments_btn.grid(row=0, column=0, pady=10)

        self.show_customers_btn = ctk.CTkButton(left_frame, text="Show All Customers", command=self.show_all_customers)
        self.show_customers_btn.grid(row=1, column=0, pady=10)

        self.show_payments_btn = ctk.CTkButton(left_frame, text="Show All Payments", command=self.show_all_payments)
        self.show_payments_btn.grid(row=2, column=0, pady=10)

        self.show_orders_btn = ctk.CTkButton(left_frame, text="Show All Orders", command=self.show_all_orders)
        self.show_orders_btn.grid(row=3, column=0, pady=10)

        # Appearance 模式切换
        appearance_mode_label = ctk.CTkLabel(left_frame, text="Appearance Mode:")
        appearance_mode_label.grid(row=5, column=0, padx=20, pady=5, sticky="w")

        self.appearance_mode_optionmenu = ctk.CTkOptionMenu(left_frame, values=["Light", "Dark", "System"],
                                                            command=self.change_appearance_mode)
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=10)
        self.appearance_mode_optionmenu.set("System")  # 设置默认值

        self.exit_btn = ctk.CTkButton(left_frame, text="Exit", command=self.quit)
        self.exit_btn.grid(row=7, column=0, pady=10, sticky="s")

        # 中间区域：显示文本框，选择 Customer的下拉框，及支付金额的输入框和提交按钮
        middle_frame = ctk.CTkFrame(self)
        middle_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")  # 中间区域可以随窗口扩展

        # 允许 middle_frame 内的控件扩展
        middle_frame.grid_columnconfigure(0, weight=1)
        middle_frame.grid_columnconfigure(1, weight=1)
        middle_frame.grid_rowconfigure(0, weight=1)

        self.textbox = ctk.CTkTextbox(middle_frame, height=300, width=400)
        self.textbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")  # 文本框随窗口扩展

        ctk.CTkLabel(middle_frame, text="Select Customer:").grid(row=1, column=0, padx=6, pady=5, sticky="w")
        self.customer_combobox = ctk.CTkComboBox(middle_frame, values=["Customer 1", "Customer 2", "Customer 3"])
        self.customer_combobox.grid(row=2, column=0, padx=6, pady=5, sticky="ew")  # 下拉框随窗口扩展

        ctk.CTkLabel(middle_frame, text="Payment Amount:").grid(row=1, column=1, padx=2, pady=5, sticky="w")
        self.payment_scale = ctk.CTkEntry(middle_frame)
        self.payment_scale.grid(row=2, column=1, padx=2, pady=5, sticky="w")

        self.add_payment = ctk.CTkButton(middle_frame, text="Commit", command=self.add_payment)
        self.add_payment.grid(row=2, column=1, padx=2, pady=5, sticky="e")

        # 右侧区域：单选按钮组、复选框和开关按钮
        right_frame = ctk.CTkFrame(self)
        right_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ns")

        ctk.CTkLabel(right_frame, text="Order Type").grid(row=0, column=0, padx=10, pady=10)
        self.order_type_var = ctk.StringVar(value="pending")
        self.radio_btn1 = ctk.CTkRadioButton(right_frame, text="Pending Orders", variable=self.order_type_var, value="pending")
        self.radio_btn1.grid(row=1, column=0, sticky="w")

        self.radio_btn2 = ctk.CTkRadioButton(right_frame, text="Completed Orders", variable=self.order_type_var, value="completed")
        self.radio_btn2.grid(row=2, column=0, sticky="w")

        self.checkbox1 = ctk.CTkCheckBox(right_frame, text="Include Paid Orders")
        self.checkbox1.grid(row=3, column=0, pady=5)

        self.switch1 = ctk.CTkSwitch(right_frame, text="Only Active Customers")
        self.switch1.grid(row=4, column=0, pady=5)

    # 按钮功能示例
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
        self.textbox.insert("end", "Payment added...\n")
	
    def change_appearance_mode(self, new_mode):
        ctk.set_appearance_mode(new_mode)

# 主函数
if __name__ == "__main__":
    controller = Controller.Controller()
    controller.load_from_files()
    app = App()
    app.mainloop()