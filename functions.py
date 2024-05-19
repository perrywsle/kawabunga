import json
from cryptography.fernet import Fernet
from tkinter import messagebox

class Customer:
    def __init__(self, name, contact, email, pickupdate, pickuptime):
        self.name = name
        self.contact = contact
        self.email = email
        self.pickupdate = pickupdate
        self.pickuptime = pickuptime
class customerDatabase:
    def __init__(self):
        self.customers = []
        self.filename = "data/customer_info.json"
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.customer_info = []
                for item in data:
                    customer = Customer(item['name'], item['contact'], item['email'], item['pickupdate'], item['pickuptime'])
                    self.customer_info.append(customer)
        except FileNotFoundError:
            self.customer_info = []

    def saveCustomerInfo(self):
        with open(self.filename, 'w') as f:
            customer_data = [{'name': customer.name, 'contact': customer.contact, 'email': customer.email, 'pickupdate': customer.pickupdate,'pickuptime': customer.pickuptime} for customer in self.customer_info]
            json.dump(customer_data, f, indent=4)
class Flowers:
    def __init__(self, flower, quantity, price):
        self.flower = flower
        self.quantity = quantity
        self.price = float(price) 
class Inventory:
    def __init__(self):
        self.filename = "data/FlowerInventory.json"
        self.inventory = []
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    flower = Flowers(item['Flower'], item['Quantity'], item['Price'])
                    self.inventory.append(flower)
        except FileNotFoundError:
            pass

    def save_inventory(self):
        data = [{'Flower': item.flower, 'Quantity': item.quantity, 'Price': item.price} for item in self.inventory]
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def update_price(self, flower_name, price):
        for item in self.inventory:
            if item.flower == flower_name.upper():
                item.price = price
                self.save_inventory()
                return
        messagebox.showinfo("Error", f"{flower_name} not found in inventory.")

    def add_item(self, flower_name, quantity, price):
        for item in self.inventory:
            if item.flower == flower_name.upper():
                item.quantity += quantity
                self.save_inventory()
                messagebox.showinfo("Success", f"{quantity} {flower_name} added to inventory.")
                return
        new_flower = Flowers(flower_name, quantity, price)
        self.inventory.append(new_flower)
        self.save_inventory()
        messagebox.showinfo("Success", f"{quantity} {flower_name} added to inventory.")

    def remove_item(self, flower_name, quantity):
        for item in self.inventory:
            if item.flower == flower_name.upper():
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    self.save_inventory()
                    messagebox.showinfo("Success", f"{quantity} {flower_name} removed from inventory.")
                    return
                else:
                    messagebox.showinfo("Error", f"Not enough {flower_name} in inventory.")
                    return
        messagebox.showinfo("Error", f"{flower_name} not found in inventory.")

    def remove_item_customerorder(self, flower_name, quantity):
        for item in self.inventory:
            if item.flower == flower_name.upper():
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    self.save_inventory()
                    return True
        return False

        

    def delete_item(self, flower_name):
        for item in self.inventory:
            if item.flower == flower_name.upper():
                if item.quantity != 0:
                    messagebox.showinfo("Item Not Empty", f"The item '{flower_name}' still has quantity. Can't delete.")
                    return
                self.inventory.remove(item)
                self.save_inventory()
                messagebox.showinfo("Success", f"'{flower_name}' removed from inventory.")
                return
        messagebox.showinfo("Error", f"{flower_name} not found in inventory.")

    def check_low_stock(self, threshold=10):
        low_stock_items = [item.flower for item in self.inventory if item.quantity < threshold]
        if low_stock_items:
            messagebox.showinfo("Low Stock Items", ', '.join(low_stock_items))
        else:
            messagebox.showinfo("Low Stock Items", "No items are in low stock.")
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