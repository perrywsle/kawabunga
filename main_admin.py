import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
import subprocess
from functions import *
from datetime import datetime
import os
import glob

class InventoryWindow(Inventory):
    def __init__(self, root, admin_ui):
        super().__init__()
        self.root = root
        self.admin_ui = admin_ui
        self.popUp = None

    def add_item(self, operation):
        if operation == "new":
            if (self.new_item_entry.get() or self.new_item_quantity_entry.get()) is None:
                messagebox.showinfo("Incomplete Input", "Please fill in the item and quantity entry.")
                return
            else:
                item = self.new_item_entry.get()
                quantity = int(self.new_item_quantity_entry.get())
                super().add_item(item, quantity)
        elif operation == None:
            quantity = int(self.quantity_entry.get())
            super().add_item(self.selected_item, quantity)

        self.update_treeview()
        self.new_item_entry.delete(0, 'end')
        self.new_item_quantity_entry.delete(0, 'end')

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
        super().delete_item(self.selected_item)
        self.update_treeview() 

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
        self.popUp = tk.Toplevel(self.root)
        self.popUp.title("Inventory Management System")
        width=200
        height=200
        screen_width = self.popUp.winfo_screenwidth()
        screen_height = self.popUp.winfo_screenheight()
        x_coordinate = (screen_width - width) // 2
        y_coordinate = (screen_height - height) // 2
        self.popUp.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")
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
        inventory_title_label = tk.Label(self.root, text="Inventory Management System", font=("times new roman",30), fg="Black", bg="green", compound=CENTER)
        inventory_title_label.pack(fill=tk.X, side=tk.TOP)

        self.inventory_tree = ttk.Treeview(inventory_frame, style="mystyle.Treeview", columns=('Item', 'Quantity'), show='headings')
        self.inventory_tree.column('Item', width=860, anchor=tk.CENTER)
        self.inventory_tree.column('Quantity', width=860, anchor=tk.CENTER)
        self.inventory_tree.heading('Item', text='Flowers', anchor=tk.CENTER)
        self.inventory_tree.heading('Quantity', text='Quantity', anchor=tk.CENTER)
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
        returnToMain.place(x=0, y=0, height=50, width=50)

class AnalyticsWindow(Report):
    def __init__(self, root, admin_ui):
        super().__init__()
        self.root = root
        self.admin_ui = admin_ui
    def generate_inv_rep(self):
        super().generate_inv_report()
    def analytics_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        analytics_frame = tk.Frame(root, bd=10, relief=tk.RIDGE)
        analytics_frame.place(x=0, y=50, height=1000, relwidth=0.9)
        analytics_title_label = tk.Label(root, text="Analytics System", font=("times new roman",30), fg="Black", bg="green", compound=CENTER)
        analytics_title_label.pack(fill=tk.X, side=tk.TOP)

        # Load the image
        self.img = PhotoImage(file="images/flower.gif")
        self.inv_report = PhotoImage(file=super().get_latest_image())

        # Latest Report
        latest_report_label = tk.Label(analytics_frame, text="Latest Inventory Report", font=("times new roman", 25), bg="green")
        latest_report_label.grid(row=0, column=0, padx=10, pady=10)
        latest_report = tk.Label(analytics_frame, image=self.inv_report)
        latest_report.grid(row=0, column=1, padx=10, pady=10)

        # Buttons
        button_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        button_frame.place(x=1725, y=50, height=900, relwidth=0.1)
        self.gen_inv_rep_button = tk.Button(button_frame, text="\nInventory Report\n", font=("times new roman", 20), command=self.generate_inv_rep, bg="light green", fg="black", cursor="hand2")
        self.gen_inv_rep_button.pack(fill=tk.X, side=tk.TOP)

        #Return to main menu
        returnToMain = tk.Button(self.root, text="<-", font=("times new roman", 20), command=self.admin_ui.returnToMain, fg="black", bg="grey", compound=LEFT)
        returnToMain.place(x=0, y=0, height=50, width=50)

class admin_UI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        self.root.state("zoomed")
        self.root = root
        self.inventoryWindwow = InventoryWindow(root, self)
        self.analyticsWindow = AnalyticsWindow(root, self)
        self.customer_database = customerDatabase()
        self.createMainMenu()
    
    def createMainMenu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.title_label = tk.Label(self.root, text="Kedai Bunga", font=("times new roman", 40, "bold"), fg="white", bg="pink")
        self.title_label.place(x=0, 
                               y=0, 
                               relwidth=1, 
                               height=self.root.winfo_screenheight()*0.07)

        # Clock Label
        current_date = datetime.now().date()
        current_time = datetime.now().time()
        self.clock_label = tk.Label(self.root, text=f"{current_date} | {current_time.strftime('%H:%M')}", font=("times new roman", 20), bg="pale violet red")
        self.clock_label.place(x=0, 
                               y=self.root.winfo_screenheight()*0.07, 
                               relwidth=1, 
                               height=self.root.winfo_screenheight()*0.08)

        # Left Menu
        left_menu = tk.Frame(self.root, bd=2, relief=tk.RIDGE, bg="white")
        left_menu.place(x=0, 
                        y=self.root.winfo_screenheight()*0.15, 
                        relwidth=0.2, 
                        height=self.root.winfo_screenheight()*0.85)

        main_panel = tk.Frame(self.root, bd=2, relief=tk.FLAT)
        main_panel.place(x=self.root.winfo_screenwidth()*0.2, y=102, relwidth=0.8, height=self.root.winfo_screenheight()-102)
        menu_label = tk.Label(left_menu, text="Menu", font=("times new roman", 20), bg="pink")
        menu_label.pack(side=tk.TOP, fill=tk.X)

        self.menu_img = tk.PhotoImage(file = "images/flower_2.gif")
        self.main_panel_img = tk.PhotoImage(file = self.analyticsWindow.get_latest_image())
        main_panel_label = tk.Label(main_panel, image=self.main_panel_img, compound=tk.CENTER)
        main_panel_label.pack(side=tk.TOP, fill=tk.X)

        # Buttons in Left Menu
        flower_label = tk.Label(left_menu, image=self.menu_img, compound=tk.CENTER)
        flower_label.pack(side=tk.TOP, fill=tk.X)
        inventory_button = tk.Button(left_menu, text="\nInventory Module\n", command=self.inventoryWindwow.inventory_window, font=("times new roman", 20), bg="blue", fg="white")
        inventory_button.pack(side=tk.TOP, fill=tk.X)
        analytics_button = tk.Button(left_menu, text="\nAnalytics\n", command=self.analyticsWindow.analytics_window, font=("times new roman", 20), bg="blue", fg="white")
        analytics_button.pack(side=tk.TOP, fill=tk.X)
        order_status_button = tk.Button(left_menu, text="\nOrders\n", font=("times new roman", 20), bg="blue", fg="white")
        order_status_button.pack(side=tk.TOP, fill=tk.X)
        customer_button = tk.Button(left_menu, text="\nCustomer Page\n", command=self.open_customer_UI, font=("times new roman", 20), bg="yellow", bd=3, cursor="hand2")
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
style = ttk.Style(root)
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=("times new roman", 20))
style.configure("mystyle.Treeview.Heading", font=("times new roman", 30,"bold"), background="light blue", foreground="green")
style.configure("mystyle.Treeview", rowheight=50)
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
root.mainloop()