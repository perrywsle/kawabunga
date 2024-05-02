import matplotlib.pyplot as plt
import numpy as np
import json
import os
from cryptography.fernet import Fernet
from tkinter import messagebox
from datetime import datetime

class Customer:
    def __init__(self, name, contact, email):
        self.name = name
        self.contact = contact
        self.email = email
       
class customerDatabase:
    def __init__(self):
        self.customers = []
        self.loadFile()

    def loadFile(self):
        self.filename = "data/customer_info.json"
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.customer_info = []
                for item in data:
                    obj = Customer(item['name'], item['contact'], item['email'])
                    self.customer_info.append(obj)
        except FileNotFoundError:
            self.customer_info = []

    def email_login(self, email):
        email = email.lower()
        if email in self.customer_info:
            return any(user.email == email for user in self.customer_info)
        
    def contact_login(self, contact):
        if contact in self.customer_info:
            return any(user.contact == contact for user in self.customer_info)

class Inventory:
    def __init__(self):
        self.filename = "data/inventory.json"
        try:
            with open(self.filename, 'r') as f:
                self.inventory = json.load(f)
        except FileNotFoundError:
            self.inventory = {}

    def save_inventory(self):
        with open(self.filename, 'w') as f:
            json.dump(self.inventory, f)

    def add_item(self, item_name, quantity):
        item = item_name.lower()
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
        messagebox.showinfo("Success", f"{quantity} {item} added to inventory.")
        self.save_inventory()

    def remove_item(self, item_name, quantity):
        item = item_name.lower()
        if item in self.inventory:
            if self.inventory[item] >= quantity:
                self.inventory[item] -= quantity
                messagebox.showinfo("Success", f"{quantity} {item} removed from inventory.")
            else:
                messagebox.showinfo(f"Error: Not enough {item} in inventory.")
        else:
            messagebox.showinfo(f"Error: {item} not found in inventory.")
        self.save_inventory()

    def check_low_stock(self, threshold=10):
        low_stock_items = [item for item, quantity in self.inventory.items() if quantity < threshold]
        if low_stock_items:
            messagebox.showinfo("Low Stock Items", ', '.join(low_stock_items))
        else:
            messagebox.showinfo("Low Stock Items", "No items are in low stock.")

class InventoryReport(Inventory):
    def generate_inv_report(self):
        # Create a bar plot for inventory items
        items = list(self.inventory.keys())
        quantities = list(self.inventory.values())

        plt.figure(figsize=(10, 6))
        plt.bar(items, quantities, color='skyblue')
        plt.xlabel('Inventory Items')
        plt.ylabel('Quantity')
        plt.title('Inventory Report')
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Ensure the directory exists
        directory = 'report'
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Save the plot as an image or display it
        plt.savefig(f'{directory}/inventory_report_{datetime.now().date()}.png')  # Save as an image
        return plt.show()  # Display the plot (uncomment if needed)

class PasswordManager:
    def __init__(self, filename='data/passwords.json', keyfile='data/key.key'):
        self.filename = filename
        try:
            with open(keyfile, 'rb') as f:
                self.key = f.read()
        except FileNotFoundError:
            self.key = Fernet.generate_key()
            with open(keyfile, 'wb') as f:
                f.write(self.key)
        self.cipher_suite = Fernet(self.key)

    def encrypt_password(self, password):
        return self.cipher_suite.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password):
        return self.cipher_suite.decrypt(encrypted_password.encode()).decode()

    def add_password(self, username, password):
        encrypted_password = self.encrypt_password(password)
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}
        data[username] = encrypted_password
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def check_password(self, username, password):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            return False
        encrypted_password = data.get(username)
        if encrypted_password is None:
            return False
        return self.decrypt_password(encrypted_password) == password

