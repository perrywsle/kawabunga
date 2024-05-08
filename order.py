import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from functions import customerDatabase, Customer, Inventory
import matplotlib.pyplot as plt
import os, glob
import json

purchaselist = []
purchaselistprice = []
class Order:
    def __init__(self):
        self.inv = Inventory()

    def click(self, a):
        purchaselist.append(a)
        price = None
        for item in self.inv.inventory:
            if item.flower == a.upper():
                price = item.price
                break
        if price is None:
            messagebox.showinfo("Error", f"{a} not found in inventory.")
            return
        purchaselistprice.append(price)
        if self.inv.remove_item_customerorder(a, 1) is not True:
            messagebox.showinfo("Error", f"Not enough {a} in inventory.")
            purchaselist.clear()
            purchaselistprice.clear()
            return
        order_confirmation = messagebox.askyesno("Order confirmation", "Are you sure you want to purchase this flower?")
        if order_confirmation:
            messagebox.showinfo("Order Purchase", "Order added to cart.")      
        else:
            del purchaselistprice[purchaselist.index(a)]
            purchaselist.remove(a)
            messagebox.showinfo("Order Purchase", "Order cancelled.")

class RegistrationWindow(Customer):
    def __init__(self, root, customer_ui):
        self.customerDatabase = customerDatabase()
        self.root = root
        self.customer_ui = customer_ui
        self.sales_file = 'data/sales.json'

    def checkoutfinal(self):
        totalvalue = sum(purchaselistprice)
        items_summary = "\n".join(f"{item} - RM {price:.2f}" for item, price in zip(purchaselist, purchaselistprice))
        if totalvalue == 0:
            messagebox.showinfo("Reminder", "No order.")
        else: 
            purchase_confirmation = messagebox.askyesno("Items selected:", f"Selected items:\n{items_summary}\nTotal value: RM {totalvalue:.2f}")
            if purchase_confirmation:
                sales = []
                if os.path.exists(self.sales_file):
                    with open(self.sales_file, 'r') as f:
                        sales = json.load(f)
                for item, price in zip(purchaselist, purchaselistprice):
                    data = {'flower': item, 'revenue':price}
                    sales.append(data)
                with open(self.sales_file, 'w') as f:
                    json.dump(sales, f, indent=4)
                messagebox.showinfo("Total amount of purchase", f"Your total purchase: RM {totalvalue:.2f}")
                self.register_popUp = tk.Toplevel(self.root)
                self.register_popUp.title("Customer Registration")
                self.name_label = tk.Label(self.register_popUp, text="Name: ", font=("times new roman", 20))
                self.name_label.grid(row=0, column=0, padx=10, pady=10)
                self.name_entry = tk.Entry(self.register_popUp, font=("Arial", 12))
                self.name_entry.grid(row=0, column=1, padx=10, pady=10)
                self.contact_label = tk.Label(self.register_popUp, text="Contact: ", font=("times new roman", 20))
                self.contact_label.grid(row=1, column=0, padx=10, pady=10)
                self.contact_entry = tk.Entry(self.register_popUp, font=("Arial", 12))
                self.contact_entry.grid(row=1, column=1, padx=10, pady=10)
                self.email_label = tk.Label(self.register_popUp, text="Email: ", font=("times new roman", 20))
                self.email_label.grid(row=2, column=0, padx=10, pady=10)
                self.email_entry = tk.Entry(self.register_popUp, font=("Arial", 12))
                self.email_entry.grid(row=2, column=1, padx=10, pady=10)
                self.submit_button = tk.Button(self.register_popUp, text="Submit", font=("times new roman", 20), command=self.register_info, cursor="hand2")
                self.submit_button.grid(row=3, column=1, padx=10, pady=10)
            else:
                purchaselist.clear()
                purchaselistprice.clear()
                messagebox.showinfo("Success", "Data cleared successfully!")

    def register_info(self):        
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        email = self.email_entry.get()
        if name in [customer.name for customer in self.customerDatabase.customer_info] or contact in [customer.contact for customer in self.customerDatabase.customer_info] or email in [customer.email for customer in self.customerDatabase.customer_info] :
            messagebox.showinfo("","Name already recorded.\nThank you for purchasing!")
        else:
            new_customer = Customer(name, contact, email)
            self.customerDatabase.customer_info.append(new_customer)
            self.customerDatabase.saveCustomerInfo()
            messagebox.showinfo("Registration Successful", f"Thank you {name} for your purchase!")
            self.register_popUp.destroy()

class Report(Inventory):
    def __init__(self):
        super().__init__()
        self.sales_file = "data/sales.json"
    def generate_inv_report(self):
        items = [item.flower for item in self.inventory]
        quantities = [item.quantity for item in self.inventory]

        plt.figure(figsize=(10, 6))
        plt.bar(items, quantities, color='skyblue')
        plt.xlabel('Inventory Items')
        plt.ylabel('Quantity')
        plt.title('Inventory Report')
        plt.xticks(rotation=90)
        plt.tight_layout()

        directory = 'report/inventory'
        if not os.path.exists(directory):
            os.makedirs(directory)

        plt.savefig(f'{directory}/inventory_report_{datetime.now().date()}.png') 
        return plt.show()

    def generate_sales_report(self):
        with open(self.sales_file, 'r') as f:
            data = json.load(f)
            self.sales = []
            for item in data:
                sale = (item['flower'], item['revenue'])
                self.sales.append(sale)

        items = [sale[0] for sale in self.sales]
        prices = [sale[1] for sale in self.sales]

        plt.figure(figsize=(10, 6))
        plt.bar(items, prices, color='skyblue')
        plt.xlabel('Items Sold')
        plt.ylabel('Revenue')
        plt.title('Sales Report')
        plt.xticks(rotation=90)
        plt.tight_layout()

        directory = 'report/sales'
        if not os.path.exists(directory):
            os.makedirs(directory)

        plt.savefig(f'{directory}/sales_report_{datetime.now().date()}.png') 
        return plt.show()
    
    def get_latest_image(self, directory):
        list_of_files = glob.glob(f'{directory}/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file
