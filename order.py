import tkinter as tk
from tkinter import *
from tkinter import messagebox
from docxtpl import DocxTemplate
import docx2pdf
from datetime import datetime
from functions import customerDatabase, Customer, Inventory
import matplotlib.pyplot as plt
import os, glob
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import re

purchaselist = []
purchaselistprice = []
# Sample data for the purchase list
purchase_list = []
class Order:
    def __init__(self):
        self.inv = Inventory()

    def click(self, a):
        purchaselist.append(a)
        price = None
        for item in self.inv.inventory:
            if item.flower == a.upper():
                if item.quantity >= 1:
                    price = item.price
                    if price is None:
                        messagebox.showinfo("Error", f"{a} not found in inventory.")
                        return
                    purchaselistprice.append(f"{price:.2f}")
                    break
                else:
                    messagebox.showinfo("Error", f"Not enough {a} in inventory.")
                    purchaselist.remove(a)
                    return

        order_confirmation = messagebox.askyesno("Order confirmation", "Are you sure you want to purchase this flower?")
        if order_confirmation:
            messagebox.showinfo("Order Purchase", "Order added to cart.")
        else:
            index = purchaselist.index(a)
            del purchaselistprice[index]
            purchaselist.remove(a)
            messagebox.showinfo("Order Purchase", "Order cancelled.")
class order_UI:
    def __init__(self, root, customer_UI):
        self.root = root
        self.customerUI = customer_UI
        self.inv = Inventory()
        self.customerDatabase = customerDatabase()
        self.sales_file = 'data/sales.json'

    def order_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create the main frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=1)

        order_title_label = tk.Label(main_frame, text="Check out page", font=("times new roman", 30), bg="pale violet red", compound=tk.CENTER)
        order_title_label.pack(fill=tk.X, side=tk.TOP)

        # Create the main frame
        order_frame = tk.Frame(main_frame, bd=2, relief=tk.RIDGE)
        order_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        canvas = tk.Canvas(main_frame)
        canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

        # Create another frame inside the canvas
        self.scrollable_frame = tk.Frame(canvas)
        self.scrollable_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
        # Add a scrollbar to the canvas
        scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.purchase_list()
            
        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.configure(scrollregion=canvas.bbox("all"))
        self.scrollable_frame.bind("<MouseWheel>", self.mouse_scroll)
        canvas.bind("<MouseWheel>", self.mouse_scroll)

        # Add that new frame to a window in the canvas
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Customer registration form
        self.name_label = tk.Label(order_frame, text="Name: ", font=("times new roman", 30))
        self.name_label.pack()
        self.name_entry = tk.Entry(order_frame, font=("Arial", 15))
        self.name_entry.pack()
        self.contact_label = tk.Label(order_frame, text="Contact: ", font=("times new roman", 30))
        self.contact_label.pack()
        self.contact_entry = tk.Entry(order_frame, font=("Arial", 15))
        self.contact_entry.pack()
        self.email_label = tk.Label(order_frame, text="Email: ", font=("times new roman", 30))
        self.email_label.pack()
        self.email_entry = tk.Entry(order_frame, font=("Arial", 15))
        self.email_entry.pack()
        self.pickupdate_label = tk.Label(order_frame, text="Pick-up date (YYYY-MM-DD): ", font=("times new roman", 30))
        self.pickupdate_label.pack()
        self.pickupdate_entry = tk.Entry(order_frame, font=("Arial", 15))
        self.pickupdate_entry.pack()
        self.pickuptime_label = tk.Label(order_frame, text="Pick-up time (HH:MM): ", font=("times new roman", 30))
        self.pickuptime_label.pack()
        self.pickuptime_entry = tk.Entry(order_frame, font=("Arial", 15))
        self.pickuptime_entry.pack()
        self.submit_button = tk.Button(order_frame, text="Submit", font=("times new roman", 30), command=self.register_info, cursor="hand2")
        self.submit_button.pack()

        # Return to main menu
        return_to_main = tk.Button(self.root, text="<-", font=("times new roman", 20), command=self.customerUI.returnToMain, fg="black", bg="grey", compound=tk.LEFT)
        return_to_main.place(x=0, y=0, height=50, width=50)
        self.scrollable_frame.bind("<Configure>", lambda event, canvas=canvas: self.customerUI.onFrameConfigure(canvas))
        
    def purchase_list(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        total_purchase_label = tk.Label(self.scrollable_frame, text="Total purchase:", font=("times new roman", 25), bg="white", compound=tk.CENTER)
        total_purchase_label.grid(row=0, column=0)

        total_price = sum(purchaselistprice)

        total_price_label = tk.Label(self.scrollable_frame, text=f"RM {total_price:.2f}", font=("times new roman", 25), bg="white", compound=tk.CENTER)
        total_price_label.grid(row=0, column=1)

        # Title just above the table
        title_label = tk.Label(self.scrollable_frame, text="Purchase List", font=("times new roman", 40), bg="pink", compound=tk.CENTER)
        title_label.grid(row=1, column=0, columnspan=2)

        purchase_list.clear()
        # Populate the scrollable frame with the updated purchase list
        for item, price in zip(purchaselist, purchaselistprice):
            price = str(f"{price:.2f}")
            data = {'flower': item, 'revenue':"RM" + price}
            purchase_list.append(data)

        # Populate the scrollable frame with the purchase list
        for i, purchase in enumerate(purchase_list):
            for j, (key, value) in enumerate(purchase.items()):
                label = tk.Label(self.scrollable_frame, text=value, font=20, padx=50, pady=35, relief=tk.RIDGE)
                label.grid(row=i + 2, column=j, sticky="nsew")
                remove_button = tk.Button(self.scrollable_frame, text="Remove", font=20, bg="light grey", padx=50, pady=35, relief=tk.FLAT, command=lambda f=purchase['flower']: self.remove_item(f))
                remove_button.grid(row=i + 2, column=j + 1)

        clear_button = tk.Button(self.root, text="Clear", font=("times new roman", 30), command = self.cancel_order, fg="black", bg="grey", compound=tk.RIGHT)
        clear_button.place(x=1400, y=750, height=50, width=100)
                
    def remove_item(self, item):
        if item in purchaselist:
            index = purchaselist.index(item)
            del purchaselistprice[index]
            purchaselist.remove(item)
            purchase_list.pop(index)
            self.purchase_list()
        else:
            messagebox.showinfo("Error", "Item not found in the purchase list.")

    def cancel_order(self):
        purchaselist.clear()
        purchaselistprice.clear()
        self.purchase_list()

    def mouse_scroll(self, event):
        canvas = event.widget
        canvas.yview_scroll(int(-1 * (event.delta // 120)), "units")
                
    def register_info(self):     
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        email = self.email_entry.get()   
        pickupdate = self.pickupdate_entry.get()
        pickuptime = self.pickuptime_entry.get()

        # remove item from inventory
        for item in purchaselist:
            self.inv.remove_item(item, 1)

        if not re.match (r"^[A-Za-z\s]*$", name):
            messagebox.showerror("Error", "Please enter a valid name with alphabetic characters only.")
            return 
        
        if not re.match (r"^\d{10}$", contact):
            messagebox.showerror("Error", "Please enter a valid numeric contact number.")
            return
        
        if not re.match (r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            messagebox.showerror("Error","Please enter a valid email address.")
            return
        
        try:
            user_date = datetime.strptime(pickupdate, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid date using the YYYY-MM-DD format.")
            return

        if user_date < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
            messagebox.showerror("Error", "Please enter a valid date.")
            return

        
        if not re.match (r"^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$", pickuptime):
            messagebox.showerror("Error", "Please enter a valid time using the HH:MM 24-hour format.")
            return

        new_customer = Customer(name, contact, email, pickupdate, pickuptime)
        new_customer.add_purchase(list(zip(purchaselist, purchaselistprice)))
        self.customerDatabase.customer_info.append(new_customer)
        self.customerDatabase.saveCustomerInfo()
        invoice_list = list(zip(purchaselist,purchaselistprice))

        #generate receipt
        doc = DocxTemplate("invoice_template 2.docx")
        print (invoice_list)
        total = sum(purchaselistprice)
        totall = f"RM {total:.2f}"
        doc.render({"name": name, 
        "phone": contact,
        "email": email,
        "collectingdate" : pickupdate,
        "collectingtime": pickuptime,
        "invoice_list" : invoice_list,
        "total": totall})

        # Create a directory for invoices if it doesn't exist
        if not os.path.exists('invoices'):
            os.makedirs('invoices')

        # Generate unique filename based on current date and time
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        docx_filename = "invoices/invoice.docx"
        pdf_filename = f"invoices/invoice_{timestamp}.pdf"

        doc.save(docx_filename)
        docx2pdf.convert(docx_filename, pdf_filename)
        messagebox.showinfo("Registration Successful", f"Thank you {name} for your purchase! Your receipt has been sent to your email.")

        sales_data = [{'flower': item, 'revenue': price} for item, price in zip(purchaselist, purchaselistprice)]
        
        # Load existing data
        with open(self.sales_file, 'r') as f:
            existing_data = json.load(f)
        
        # Append new data
        existing_data.extend(sales_data)
        
        # Write everything back to the file
        with open(self.sales_file, 'w') as f:
            json.dump(existing_data, f, indent=4)

        # send email to customer
        smtp_port = 587                
        smtp_server = "smtp.gmail.com"  

        email_from = "siewchingpang05@gmail.com"
        email_to = [email]

        password = "vnzh asil wbbl rczk"

        subject = "Email from Kawabunga with receipt!"

        def send_emails(email_to):

            for person in email_to:

            # Make the body of the email
                body = f"""
                Dear customer,

                Here is your order receipt.
                Please bring your receipt to collect your order and pay on spot. 
                """

                message = MIMEMultipart()
                message['From'] = email_from
                message['To'] = person
                message['Subject'] = subject

                message.attach(MIMEText(body, 'plain'))

                filename = pdf_filename

                receipt = open(filename, 'rb') 

                receipt_package = MIMEBase('application', 'octet-stream')
                receipt_package.set_payload((receipt).read())
                encoders.encode_base64(receipt_package)
                receipt_package.add_header('Content-Disposition', "receipt; filename= " + filename)
                message.attach(receipt_package)

                text = message.as_string()

                print("Connecting to server...")
                Kawabunga = smtplib.SMTP(smtp_server, smtp_port)
                Kawabunga.starttls()
                Kawabunga.login(email_from, password)
                print("Succesfully connected to server")
                print()

                print(f"Sending email to: {person}...")
                Kawabunga.sendmail(email_from, person, text)
                print(f"Email sent to: {person}")
                print()

                Kawabunga.quit()

        send_emails(email_to) 

        for widget in self.root.winfo_children():
            widget.destroy()
        self.customerUI.createMainMenu()

class Report(Inventory):
    def __init__(self):
        super().__init__()
        self.sales_file = "data/sales.json"
    def generate_inv_report(self):
        items = [item.flower for item in self.inventory]
        quantities = [item.quantity for item in self.inventory]

        plt.figure(figsize=(10, 6))
        plt.bar(items, quantities, color='skyblue')
        plt.xlabel('Flowers')
        plt.ylabel('Quantity')
        plt.title('Inventory Report')
        plt.xticks(rotation=90)
        plt.tight_layout()

        directory = 'report/inventory'
        if not os.path.exists(directory):
            os.makedirs(directory)

        plt.savefig(f'{directory}/inventory_report_{datetime.now().date()}.png') 

    def generate_sales_report(self):
        with open("data/sales.json", 'r') as f:
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
        plt.ylabel('Revenue (RM)')
        plt.title('Sales Report')
        plt.xticks(rotation=90)
        plt.tight_layout()

        directory = 'report/sales'
        if not os.path.exists(directory):
            os.makedirs(directory)

        plt.savefig(f'{directory}/sales_report_{datetime.now().date()}.png') 
    
    def get_latest_image(self, directory):
        list_of_files = glob.glob(f'{directory}/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file
