import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
import subprocess
from functions import Inventory, InventoryReport, Customer, customerDatabase, PasswordManager
from datetime import datetime

class InventoryWindow(Inventory):
    def __init__(self, root, admin_ui):
        super().__init__()
        self.root = root
        self.admin_ui = admin_ui
        self.popUp = None

    def add_item(self, operation):
        if operation == "new":
            if (self.new_item_entry.get() and self.new_item_quantity_entry.get()) is not None:
                item = self.new_item_entry.get()
                quantity = int(self.new_item_quantity_entry.get())
                super().add_item(item, quantity)
        elif operation == None:
            quantity = int(self.quantity_entry.get())
            super().add_item(self.selected_item, quantity)

        self.update_treeview()
        self.new_item_entry.delete(0, 'end')
        self.new_item_quantity_entry.delete(0, 'end')
        self.popUp.destroy()

    def remove_item(self):
        quantity = int(self.quantity_entry.get())
        super().remove_item(self.selected_item, quantity)
        self.update_treeview()  
        self.quantity_entry.delete(0, 'end')
        self.popUp.destroy()

    def delete_item(self):
        if not self.inventory_tree.selection():
            messagebox.showinfo("No Selection", "Please select an item in the inventory.")
            return
        item_name = self.inventory_tree.item(self.inventory_tree.selection())['values'][0]
        if self.inventory[item_name] != 0:
            messagebox.showinfo("Item Not Empty", f"The item '{item_name}' still has quantity. Can't delete.")
            return
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{item_name}' from the inventory?")
        if confirm:
            del self.inventory[item_name]
            super().save_inventory()
            self.update_treeview()
            messagebox.showinfo("Success", f"'{item_name}' removed from inventory.")

    def update_treeview(self):
        for i in self.inventory_tree.get_children():
            self.inventory_tree.delete(i)
        for item, quantity in self.inventory.items():
            self.inventory_tree.insert('', 'end', values=(item, quantity))

    def popUp_window(self, operation):
        if not self.inventory_tree.selection():
            messagebox.showinfo("No selection", "Please select an item in the inventory")
            return 
        if self.popUp is not None:
            self.popUp.destroy()
        self.popUp= tk.Toplevel(self.root)
        self.popUp.title("Inventory Management System")
        self.quantity_entry_label = tk.Label(self.popUp, text="Quantity: ", font=("times new roman", 20))
        self.quantity_entry_label.pack(pady=10, padx=20, fill=tk.X)
        self.quantity_entry = tk.Entry(self.popUp, font=("Arial", 12))
        self.quantity_entry.pack(pady=10, padx=20, fill=tk.X)
        if operation == "add":
            confirm_button = tk.Button(self.popUp, text="Confirm", command=lambda: self.add_item(None), font=("times new roman", 20))
        else:
            confirm_button = tk.Button(self.popUp, text="Confirm", command=self.remove_item, font=("times new roman", 20))
        confirm_button.pack(pady=10, padx=20, side=tk.RIGHT)

    def on_tree_select(self, event):
        self.selected_item = self.inventory_tree.item(self.inventory_tree.selection())['values'][0]
        return True

    def inventory_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        inventory_frame = tk.Frame(self.root, bd=20, relief=tk.RIDGE)
        inventory_frame.place(x=0, y=50, height=1000, relwidth=0.9)
        self.inventory_tree = ttk.Treeview(inventory_frame, columns=('Item', 'Quantity'), show='headings')
        self.inventory_tree.column('Item', width=860)
        self.inventory_tree.column('Quantity', width=860)
        self.inventory_tree.heading('Item', text='Item')
        self.inventory_tree.heading('Quantity', text='Quantity')
        self.inventory_tree.pack(fill=tk.X, side=tk.LEFT)
        self.inventory_tree.bind('<<TreeviewSelect>>', self.on_tree_select)

        button_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        button_frame.place(x=1725, y=50, height=900, relwidth=0.1)
        self.add_item_button = tk.Button(button_frame, text="+", command=lambda: self.popUp_window("add"), font=("times new roman", 40))
        self.add_item_button.pack(fill=tk.X, side=tk.TOP)
        self.remove_item_button = tk.Button(button_frame, text="-", command=lambda: self.popUp_window("remove"), font=("times new roman", 40))
        self.remove_item_button.pack(fill=tk.X, side=tk.TOP)

        self.update_treeview()

        self.new_item_quantity_entry = tk.Entry(button_frame, font=("Arial", 20))
        self.new_item_quantity_entry.pack(fill=tk.X, side=tk.BOTTOM)  
        self.new_item_entry = tk.Entry(button_frame, font=("Arial", 20))
        self.new_item_entry.pack(fill=tk.X, side=tk.BOTTOM) 

        self.new_item_button = tk.Button(button_frame, text="Add new item", command=lambda: self.add_item("new"), font=("times new roman", 20), bg="pink")
        self.new_item_button.pack(fill=tk.X, side=tk.BOTTOM)

        self.delete_item_button = tk.Button(button_frame, text="Delete", command=self.delete_item, font=("times new roman", 20), bg="red")
        self.delete_item_button.pack(fill=tk.X, side=tk.BOTTOM)

        self.check_low_stock_button = tk.Button(button_frame, text="Check low stock", command=super().check_low_stock, font=("times new roman", 20), bg="pale violet red")
        self.check_low_stock_button.pack(fill=tk.X, side=tk.TOP)

        returnToMain = tk.Button(self.root, text="<-", font=("times new roman", 20), command=self.admin_ui.returnToMain, fg="black", bg="yellow", compound=LEFT)
        returnToMain.place(x=10, y=10, height=50, width=50)

class AnalyticsWindow(InventoryReport):
    def __init__(self, root, admin_ui):
        super().__init__()
        self.root = root
        self.admin_ui = admin_ui
    def generate_inv_rep(self):
        super().generate_inv_report()
    def analytics_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Load the image
        self.img = PhotoImage(file= r"images\flower.gif")
        # Design
        title_frame = tk.Frame(self.root, bg="#010c48")
        title_frame.pack(fill=tk.X)
        # Create a label for the image
        img_label = tk.Label(title_frame, image=self.img, bg="#010c48")
        img_label.grid(row=0, column=0, padx=10, pady=10)
        # Create a label for the title
        title = tk.Label(title_frame, text="Analytics", font=("times new roman", 40, "bold"), fg="white", bg="#010c48", compound="left")
        title.grid(row=0, column=1, padx=10, pady=10)
        # Buttons
        self.inv_report_button = tk.Button(root, text="Inventory Report", command=self.generate_inv_rep, bg="blue", fg="white", font=("Arial", 14))
        self.inv_report_button.pack(pady=10, padx=20, fill=tk.X)

        #Return to main menu
        returnToMain = tk.Button(self.root, text="<-", font=("times new roman", 20), command=self.admin_ui.returnToMain, fg="black", bg="yellow", compound=LEFT)
        returnToMain.place(x=10, y=10, height=50, width=50)

class admin_UI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        self.root.state("zoomed")
        self.root = root
        self.inventoryWindwow = InventoryWindow(root, self)
        self.analyticsWindow = AnalyticsWindow(root, self)
        self.customer_database = customerDatabase()
        self.password_manager = PasswordManager()
        self.loginPage()
    
    def loginPage(self):
        self.login_frame = tk.Frame(self.root, bd=10, relief=tk.FLAT)
        self.login_frame.pack(side=TOP)
        self.login_label = tk.Label(self.login_frame, text="\n\n\n\n\nLogin", font=("times new roman", 30))
        self.login_label.pack(side=TOP, fill=tk.X)
        self.admin_name_entry = tk.Entry(self.login_frame, font=("times new roman", 30))
        self.admin_name_entry.pack(side=TOP, fill=tk.X)
        self.admin_password_entry = tk.Entry(self.login_frame, font=("times new roman", 30))
        self.admin_password_entry.pack(side=TOP, fill=tk.X)
        self.login_button = tk.Button(self.login_frame, text="Login", font=("times new roman", 30), command=self.attemptLogin)
        self.login_button.pack(side=BOTTOM)

    def attemptLogin(self):
        admin_name = self.admin_name_entry.get()
        admin_password = self.admin_password_entry.get()
        if self.password_manager.check_password(admin_name, admin_password):
            self.createMainMenu()
        else:
            exit()

    def createMainMenu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        # Title Label
        self.title_label = tk.Label(self.root, text="Kedai Bunga", font=("times new roman", 40, "bold"), fg="white", bg="pink")
        self.title_label.place(x=0, y=0, relwidth=1, height=70)

        # Log Out Button (myb change to contact smth like that)
        self.logout_button = tk.Button(self.root, text="Log Out", font=("times new roman", 15, "bold"), bg="yellow", compound=CENTER, cursor="hand2")
        self.logout_button.place(x=1770, y=0, height=70, width=150)

        # Clock Label
        current_date = datetime.now().date()
        current_time = datetime.now().time()
        self.clock_label = tk.Label(self.root, text=f"{current_date} | {current_time.strftime('%H:%M:%S')}", font=("times new roman", 20), bg="pale violet red")
        self.clock_label.place(x=0, y=70, relwidth=1, height=30)

        # Create Treeview
        """table_frame = tk.Frame(self.root, bd=100, relief=tk.FLAT)
        table_frame.place(x=500, y=102, width=1500, height=1565)
        self.notice_board_table = ttk.Treeview(self.root, columns=('no', 'notice'), show='headings')
        self.notice_board_table.column('no', width=20)
        self.notice_board_table.column('notice', width=900)
        self.notice_board_table.heading('No', text='No')
        self.notice_board_table.heading('Notice', text='Notice')
        self.notice_board_table.pack(pady=10, padx=20, fill=tk.X)"""

        # Left Menu
        left_menu = tk.Frame(self.root, bd=2, relief=tk.RIDGE, bg="white")
        left_menu.place(x=0, y=102, width=200, height=565)
        menu_label = tk.Label(left_menu, text="Menu", font=("times new roman", 20), bg="#009688")
        menu_label.pack(side=tk.TOP, fill=tk.X)

        self.menu_img = PhotoImage(file = r"images/flower_2.gif")

        # Buttons in Left Menu
        flower_label = tk.Label(left_menu, image=self.menu_img, compound=CENTER)
        flower_label.pack(side=tk.TOP, fill=tk.X)
        inventory_button = tk.Button(left_menu, text="Inventory Module", command=self.inventoryWindwow.inventory_window, font=("times new roman", 20), bg="blue", fg="white")
        inventory_button.pack(side=tk.TOP, fill=tk.X)
        analytics_button = tk.Button(left_menu, text="Analytics", command=self.analyticsWindow.analytics_window, font=("times new roman", 20), bg="blue", fg="white")
        analytics_button.pack(side=tk.TOP, fill=tk.X)
        order_status_button = tk.Button(left_menu, text="Orders", font=("times new roman", 20), bg="blue", fg="white")
        order_status_button.pack(side=tk.TOP, fill=tk.X)
        customer_button = tk.Button(left_menu, text="Customer Page", command=self.open_customer_UI, font=("times new roman", 20), bg="yellow", bd=3, cursor="hand2")
        customer_button.pack(side=tk.BOTTOM, fill=tk.X)

    def returnToMain(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.createMainMenu()
    def open_customer_UI(self):
        subprocess.Popen(["python", "main_customer.py"])
        exit()


root = tk.Tk()
app = admin_UI(root)
root.mainloop()