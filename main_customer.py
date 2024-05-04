import subprocess
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from functions import customerDatabase, Customer

purchaselistprice=[]
purchaselist=[]
flowerprice = {"B001": 499.00, "B002": 379.00,"B003": 1329.00,"B004": 399.00,"B005": 389.00,"B006": 399.00,"B007": 779.00,"B008": 159.00,"B009": 189.00,"B010": 229.00,"B011": 179.00,"B012": 399.00,"B013": 399.00,"B014": 389.00, 
    "B015": 179.00,"B016": 249.00,"B017": 199.00,"B018": 229.00,"B019": 299.00,"B020": 179.00, "F001": 439.00,"F002": 289.00,"F003": 699.00, "F004": 639.00,"F005": 439.00,"F006": 219.00, "F007": 269.00,
    "F008": 259.00,"F009": 759.00,"F010": 679.00, "F011": 389.00,"F012": 599.00, "F013": 799.00, "F014": 899.00,"F015": 1129.00,"F016": 399.00,"F017": 359.00,"F018": 499.00,"F019": 399.00,"F020": 499.00,
    "F021": 259.00,"F022": 499.00, "F023": 389.00, "F024": 559.00,"G001": 359.00,"G002": 169.00, "G003": 229.00,"G004": 699.00,"G005": 69.00, "G006": 179.00,"G007": 269.00,"G008": 129.00,"G009": 479.00,
    "G010": 129.00,"G011": 249.00,"G012": 229.00,"G013": 469.00,"G014": 169.00,"G015": 179.00,"G016": 199.00,"G017": 229.00,"G018": 129.00, "G019": 199.00,"G020": 349.00}

def click(a):
    order_confirmation = messagebox.askyesno("Order confirmation","Are you sure you want to purchase this flower?")
    if order_confirmation:
        purchaselist.append(a)
        purchaselistprice.append(flowerprice[a])
        print(purchaselistprice)
        messagebox.showinfo("Order Purchase", "Order added to cart.")

    else:
        messagebox.showinfo("Order Purchase", "Order cancelled.")
class funeralWindow:
    def __init__(self, root, customer_ui):
        self.root = root
        self.customer_ui = customer_ui

    def funeral_window(self):
        # Funeral label
        funeral_label = tk.Label(self.root, text="Funeral", font=("times new roman", 30), bg="pale violet red")
        funeral_label.pack(fill=tk.X, side=tk.TOP)

        # Create the main frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=1)

        # Create a canvas
        canvas = tk.Canvas(main_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Add a scrollbar to the canvas
        scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind_all("<MouseWheel>", self.customer_ui.mouse_scroll)

        # Create another frame inside the canvas
        scrollable_frame = tk.Frame(canvas)

        # Add that new frame to a window in the canvas
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        #Return to main menu
        returnToMain = tk.Button(self.root, text="<-", font=("times new roman", 20), command=self.customer_ui.returnToMain, fg="black", bg="yellow", compound=LEFT)
        returnToMain.place(x=10, y=10, height=50, width=50)

        # Birthday bouquet images
        self.img1 = tk.PhotoImage(file="images/funeral_sy173.gif")
        self.img2 = tk.PhotoImage(file="images/funeral_sy216.gif")
        self.img3 = tk.PhotoImage(file="images/funeral_sy231.gif")
        self.img4 = tk.PhotoImage(file="images/funeral_sy242.gif")
        self.img5 = tk.PhotoImage(file="images/funeral_sy244.gif")
        self.img6 = tk.PhotoImage(file="images/funeral_sy245.gif")
        self.img7 = tk.PhotoImage(file="images/funeral_sy248.gif")
        self.img8 = tk.PhotoImage(file="images/funeral_sy250.gif")
        self.img9 = tk.PhotoImage(file="images/funeral_sy182.gif")
        self.img10 = tk.PhotoImage(file="images/funeral_sy151.gif")
        self.img11 = tk.PhotoImage(file="images/funeral_sy143.gif")
        self.img12 = tk.PhotoImage(file="images/funeral_sy135.gif")
        self.img13 = tk.PhotoImage(file="images/funeral_sy137.gif")
        self.img14 = tk.PhotoImage(file="images/funeral_sy086.gif")
        self.img15 = tk.PhotoImage(file="images/funeral_sy121.gif")
        self.img16 = tk.PhotoImage(file="images/funeral_sy106.gif")
        self.img17 = tk.PhotoImage(file="images/funeral_sy095.gif")
        self.img18 = tk.PhotoImage(file="images/funeral_sy079.gif")
        self.img19 = tk.PhotoImage(file="images/funeral_sy062.gif")
        self.img20 = tk.PhotoImage(file="images/funeral_sy059.gif")
        self.img21 = tk.PhotoImage(file="images/funeral_sy003.gif")
        self.img22 = tk.PhotoImage(file="images/funeral_sy065.gif")
        self.img23 = tk.PhotoImage(file="images/funeral_sy075.gif")
        self.img24 = tk.PhotoImage(file="images/funeral_sy103.gif")

        # Buttons for bouquets
        funeral_flower_1 = tk.Button(scrollable_frame, image=self.img1, command=lambda: click("F001"))
        funeral_flower_1.grid(row=0, column=0, padx=10, pady=10)
        funeral_flower_1_label = tk.Label(scrollable_frame, text="F001 - RM 439.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_1_label.grid(row=1, column=0, padx=10)
        
        funeral_flower_2 = tk.Button(scrollable_frame, image=self.img2, command=lambda: click("F002"))
        funeral_flower_2.grid(row=0, column=3, padx=10, pady=10)
        funeral_flower_2_label = tk.Label(scrollable_frame, text="F002 - RM 289.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_2_label.grid(row=1, column=3, padx=10)

        funeral_flower_3 = tk.Button(scrollable_frame, image=self.img3, command=lambda: click("F003"))
        funeral_flower_3.grid(row=0, column=6, padx=10, pady=10)
        funeral_flower_3_label = tk.Label(scrollable_frame, text="F003 - RM 699.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_3_label.grid(row=1, column=6, padx=10)

        funeral_flower_4 = tk.Button(scrollable_frame, image=self.img4, command=lambda: click("F004"))
        funeral_flower_4.grid(row=0, column=9, padx=10, pady=10)
        funeral_flower_4_label = tk.Label(scrollable_frame, text="F004 - RM 639.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_4_label.grid(row=1, column=9, padx=10)

        funeral_flower_5 = tk.Button(scrollable_frame, image=self.img5, command=lambda: click("F005"))
        funeral_flower_5.grid(row=0, column=12, padx=10, pady=10)
        funeral_flower_5_label = tk.Label(scrollable_frame, text="F005 - RM 439.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_5_label.grid(row=1, column=12, padx=10)

        funeral_flower_6 = tk.Button(scrollable_frame, image=self.img6, command=lambda: click("F006"))
        funeral_flower_6.grid(row=0, column=15, padx=10, pady=10)
        funeral_flower_6_label = tk.Label(scrollable_frame, text="F006 - RM 219.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_6_label.grid(row=1, column=15, padx=10)

        funeral_flower_7 = tk.Button(scrollable_frame, image=self.img7, command=lambda: click("F007"))
        funeral_flower_7.grid(row=3, column=0, padx=10, pady=10)
        funeral_flower_7_label = tk.Label(scrollable_frame, text="F007 - RM 269.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_7_label.grid(row=4, column=0, padx=10)

        funeral_flower_8 = tk.Button(scrollable_frame, image=self.img8, command=lambda: click("F008"))
        funeral_flower_8.grid(row=3, column=3, padx=10, pady=10)
        funeral_flower_8_label = tk.Label(scrollable_frame, text="F008 - RM 259.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_8_label.grid(row=4, column=3, padx=10)

        funeral_flower_9 = tk.Button(scrollable_frame, image=self.img9, command=lambda: click("F009"))
        funeral_flower_9.grid(row=3, column=6, padx=10, pady=10)
        funeral_flower_9_label = tk.Label(scrollable_frame, text="F009 - RM 759.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_9_label.grid(row=4, column=6, padx=10)

        funeral_flower_10 = tk.Button(scrollable_frame, image=self.img10, command=lambda: click("F010"))
        funeral_flower_10.grid(row=3, column=9, padx=10, pady=10)
        funeral_flower_10_label = tk.Label(scrollable_frame, text="F010 - RM 679.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_10_label.grid(row=4, column=9, padx=10)

        funeral_flower_11 = tk.Button(scrollable_frame, image=self.img11, command=lambda: click("F011"))
        funeral_flower_11.grid(row=3, column=12, padx=10, pady=10)
        funeral_flower_11_label = tk.Label(scrollable_frame, text="F011 - RM 389.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_11_label.grid(row=4, column=12, padx=10)

        funeral_flower_12 = tk.Button(scrollable_frame, image=self.img12, command=lambda: click("F012"))
        funeral_flower_12.grid(row=3, column=15, padx=10, pady=10)
        funeral_flower_12_label = tk.Label(scrollable_frame, text="F012 - RM 599.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_12_label.grid(row=4, column=15, padx=10)

        funeral_flower_13 = tk.Button(scrollable_frame, image=self.img13, command=lambda: click("F013"))
        funeral_flower_13.grid(row=6, column=0, padx=10, pady=10)
        funeral_flower_13_label = tk.Label(scrollable_frame, text="F013 - RM 799.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_13_label.grid(row=7, column=0, padx=10)

        funeral_flower_14 = tk.Button(scrollable_frame, image=self.img14, command=lambda: click("F014"))
        funeral_flower_14.grid(row=6, column=3, padx=10, pady=10)
        funeral_flower_14_label = tk.Label(scrollable_frame, text="F014 - RM 899.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_14_label.grid(row=7, column=3, padx=10)

        funeral_flower_15 = tk.Button(scrollable_frame, image=self.img15, command=lambda: click("F015"))
        funeral_flower_15.grid(row=6, column=6, padx=10, pady=10)
        funeral_flower_15_label = tk.Label(scrollable_frame, text="F015 - RM 1129.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_15_label.grid(row=7, column=6, padx=10)

        funeral_flower_16 = tk.Button(scrollable_frame, image=self.img16, command=lambda: click("F016"))
        funeral_flower_16.grid(row=6, column=9, padx=10, pady=10)
        funeral_flower_16_label = tk.Label(scrollable_frame, text="F016 - RM 399.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_16_label.grid(row=7, column=9, padx=10)

        funeral_flower_17 = tk.Button(scrollable_frame, image=self.img17, command=lambda: click("F017"))
        funeral_flower_17.grid(row=6, column=12, padx=10, pady=10)
        funeral_flower_17_label = tk.Label(scrollable_frame, text="F017 - RM 359.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_17_label.grid(row=7, column=12, padx=10)

        funeral_flower_18 = tk.Button(scrollable_frame, image=self.img18, command=lambda: click("F018"))
        funeral_flower_18.grid(row=6, column=15, padx=10, pady=10)
        funeral_flower_18_label = tk.Label(scrollable_frame, text="F018 - RM 499.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_18_label.grid(row=7, column=15, padx=10)

        funeral_flower_19 = tk.Button(scrollable_frame, image=self.img19, command=lambda: click("F019"))
        funeral_flower_19.grid(row=9, column=0, padx=10, pady=10)
        funeral_flower_19_label = tk.Label(scrollable_frame, text="F019 - RM 399.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_19_label.grid(row=10, column=0, padx=10)

        funeral_flower_20 = tk.Button(scrollable_frame, image=self.img20, command=lambda: click("F020"))
        funeral_flower_20.grid(row=9, column=3, padx=10, pady=10)
        funeral_flower_20_label = tk.Label(scrollable_frame, text="F020 - RM 499.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_20_label.grid(row=10, column=3, padx=10)

        funeral_flower_21 = tk.Button(scrollable_frame, image=self.img21, command=lambda: click("F021"))
        funeral_flower_21.grid(row=9, column=6, padx=10, pady=10)
        funeral_flower_21_label = tk.Label(scrollable_frame, text="F021 - RM 259.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_21_label.grid(row=10, column=6, padx=10)

        funeral_flower_22 = tk.Button(scrollable_frame, image=self.img22, command=lambda: click("F022"))
        funeral_flower_22.grid(row=9, column=9, padx=10, pady=10)
        funeral_flower_22_label = tk.Label(scrollable_frame, text="F022 - RM 499.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_22_label.grid(row=10, column=9, padx=10)

        funeral_flower_23 = tk.Button(scrollable_frame, image=self.img23, command=lambda: click("F023"))
        funeral_flower_23.grid(row=9, column=12, padx=10, pady=10)
        funeral_flower_23_label = tk.Label(scrollable_frame, text="F023 - RM 389.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_23_label.grid(row=10, column=12, padx=10)

        funeral_flower_24 = tk.Button(scrollable_frame, image=self.img24, command=lambda: click("F024"))
        funeral_flower_24.grid(row=9, column=15, padx=10, pady=10)
        funeral_flower_24_label = tk.Label(scrollable_frame, text="F024 - RM 559.00", font=("times new roman", 20), fg="white", bg="black")
        funeral_flower_24_label.grid(row=10, column=15, padx=10)

        # Ensure that the images are kept in memory
        funeral_flower_1.image = self.img1
        funeral_flower_2.image = self.img2
        funeral_flower_3.image = self.img3
        funeral_flower_4.image = self.img4
        funeral_flower_5.image = self.img5
        funeral_flower_6.image = self.img6
        funeral_flower_7.image = self.img7
        funeral_flower_8.image = self.img8
        funeral_flower_9.image = self.img9
        funeral_flower_10.image = self.img10
        funeral_flower_11.image = self.img11
        funeral_flower_12.image = self.img12
        funeral_flower_13.image = self.img13
        funeral_flower_14.image = self.img14
        funeral_flower_15.image = self.img15
        funeral_flower_16.image = self.img16
        funeral_flower_17.image = self.img17
        funeral_flower_18.image = self.img18
        funeral_flower_19.image = self.img19
        funeral_flower_20.image = self.img20
        funeral_flower_21.image = self.img21
        funeral_flower_22.image = self.img22
        funeral_flower_23.image = self.img23
        funeral_flower_24.image = self.img24

        # Update the scroll region of the canvas
        scrollable_frame.bind("<Configure>", lambda event, canvas=canvas: self.customer_ui.onFrameConfigure(canvas))
class birthdayWindow:
    def __init__(self, root, customer_ui):
        self.root = root
        self.customer_ui = customer_ui

    def birthday_window(self):
        # Birthday label
        birthday_label = tk.Label(self.root, text="Birthday", font=("times new roman", 30), bg="pale violet red")
        birthday_label.pack(fill=tk.X, side=tk.TOP)

        # Create the main frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=1)

        # Create a canvas
        canvas = tk.Canvas(main_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Add a scrollbar to the canvas
        scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind_all("<MouseWheel>", self.customer_ui.mouse_scroll)

        # Create another frame inside the canvas
        scrollable_frame = tk.Frame(canvas)

        # Add that new frame to a window in the canvas
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        #Return to main menu
        returnToMain = tk.Button(self.root, text="<-", font=("times new roman", 20), command=self.customer_ui.returnToMain, fg="black", bg="yellow", compound=LEFT)
        returnToMain.place(x=10, y=10, height=50, width=50)
    
        # Birthday bouquet images
        self.img1a = tk.PhotoImage(file="images/td470.gif")
        self.img2 = tk.PhotoImage(file="images/bk058.gif")
        self.img3 = tk.PhotoImage(file="images/bk194.gif")
        self.img4 = tk.PhotoImage(file="images/bk192.gif")
        self.img5 = tk.PhotoImage(file="images/bk029.gif")
        self.img6 = tk.PhotoImage(file="images/bq718.gif")
        self.img7 = tk.PhotoImage(file="images/bq707.gif")
        self.img8 = tk.PhotoImage(file="images/td463.gif")
        self.img9 = tk.PhotoImage(file="images/bq669.gif")
        self.img10 = tk.PhotoImage(file="images/bk953.gif")
        self.img11 = tk.PhotoImage(file="images/bk942.gif")
        self.img12 = tk.PhotoImage(file="images/bk928.gif")
        self.img13 = tk.PhotoImage(file="images/bk931.gif")
        self.img14 = tk.PhotoImage(file="images/bq652.gif")
        self.img15 = tk.PhotoImage(file="images/bk910.gif")
        self.img16 = tk.PhotoImage(file="images/bq648.gif")
        self.img17 = tk.PhotoImage(file="images/bk899.gif")
        self.img18 = tk.PhotoImage(file="images/bq634.gif")
        self.img19 = tk.PhotoImage(file="images/bq620.gif")
        self.img20 = tk.PhotoImage(file="images/td441.gif")

        # Buttons for bouquets
        birthday_flower_1 = tk.Button(scrollable_frame, image=self.img1a, command=lambda: click("B001"))
        birthday_flower_1.grid(row=0, column=0, padx=10, pady=10)
        birthday_flower_1_label = tk.Label(scrollable_frame, text="B001 - RM 499.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_1_label.grid(row=1, column=0, padx=10)
        
        birthday_flower_2 = tk.Button(scrollable_frame, image=self.img2, command=lambda: click("B002"))
        birthday_flower_2.grid(row=0, column=3, padx=10, pady=10)
        birthday_flower_2_label = tk.Label(scrollable_frame, text="B002 - RM 379.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_2_label.grid(row=1, column=3, padx=10)

        birthday_flower_3 = tk.Button(scrollable_frame, image=self.img3, command=lambda: click("B003"))
        birthday_flower_3.grid(row=0, column=6, padx=10, pady=10)
        birthday_flower_3_label = tk.Label(scrollable_frame, text="B003 - RM1329.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_3_label.grid(row=1, column=6, padx=10)

        birthday_flower_4 = tk.Button(scrollable_frame, image=self.img4, command=lambda: click("B004"))
        birthday_flower_4.grid(row=0, column=9, padx=10, pady=10)
        birthday_flower_4_label = tk.Label(scrollable_frame, text="B004 - RM 399.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_4_label.grid(row=1, column=9, padx=10)

        birthday_flower_5 = tk.Button(scrollable_frame, image=self.img5, command=lambda: click("B005"))
        birthday_flower_5.grid(row=0, column=12, padx=10, pady=10)
        birthday_flower_5_label = tk.Label(scrollable_frame, text="B005 - RM 389.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_5_label.grid(row=1, column=12, padx=10)

        birthday_flower_6 = tk.Button(scrollable_frame, image=self.img6, command=lambda: click("B006"))            
        birthday_flower_6.grid(row=3, column=0, padx=10, pady=10)
        birthday_flower_6_label = tk.Label(scrollable_frame, text="B006 - RM 399.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_6_label.grid(row=4, column=0, padx=10)

        birthday_flower_7 = tk.Button(scrollable_frame, image=self.img7, command=lambda: click("B007"))
        birthday_flower_7.grid(row=3, column=3, padx=10, pady=10)
        birthday_flower_7_label = tk.Label(scrollable_frame, text="B007 - RM 779.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_7_label.grid(row=4, column=3, padx=10)

        birthday_flower_8 = tk.Button(scrollable_frame, image=self.img8, command=lambda: click("B008"))
        birthday_flower_8.grid(row=3, column=6, padx=10, pady=10)
        birthday_flower_8_label = tk.Label(scrollable_frame, text="B008 - RM 159.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_8_label.grid(row=4, column=6, padx=10)

        birthday_flower_9 = tk.Button(scrollable_frame, image=self.img9, command=lambda: click("B009"))
        birthday_flower_9.grid(row=3, column=9, padx=10, pady=10)
        birthday_flower_9_label = tk.Label(scrollable_frame, text="B009 - RM 189.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_9_label.grid(row=4, column=9, padx=10)

        birthday_flower_10 = tk.Button(scrollable_frame, image=self.img10, command=lambda: click("B010"))
        birthday_flower_10.grid(row=3, column=12, padx=10, pady=10)
        birthday_flower_10_label = tk.Label(scrollable_frame, text="B010 - RM 229.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_10_label.grid(row=4, column=12, padx=10)

        birthday_flower_11 = tk.Button(scrollable_frame, image=self.img11, command=lambda: click("B011"))
        birthday_flower_11.grid(row=6, column=0, padx=10, pady=10)
        birthday_flower_11_label = tk.Label(scrollable_frame, text="B011 - RM 179.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_11_label.grid(row=7, column=0, padx=10)

        birthday_flower_12 = tk.Button(scrollable_frame, image=self.img12, command=lambda: click("B012"))
        birthday_flower_12.grid(row=6, column=3, padx=10, pady=10)
        birthday_flower_12_label = tk.Label(scrollable_frame, text="B012 - RM 399.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_12_label.grid(row=7, column=3, padx=10)

        birthday_flower_13 = tk.Button(scrollable_frame, image=self.img13, command=lambda: click("B013"))
        birthday_flower_13.grid(row=6, column=6, padx=10, pady=10)
        birthday_flower_13_label = tk.Label(scrollable_frame, text="B013 - RM 399.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_13_label.grid(row=7, column=6, padx=10)

        birthday_flower_14 = tk.Button(scrollable_frame, image=self.img14, command=lambda: click("B014"))
        birthday_flower_14.grid(row=6, column=9, padx=10, pady=10)
        birthday_flower_14_label = tk.Label(scrollable_frame, text="B014 - RM 389.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_14_label.grid(row=7, column=9, padx=10)

        birthday_flower_15 = tk.Button(scrollable_frame, image=self.img15, command=lambda: click("B015"))
        birthday_flower_15.grid(row=6, column=12, padx=10, pady=10)
        birthday_flower_15_label = tk.Label(scrollable_frame, text="B015 - RM 179.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_15_label.grid(row=7, column=12, padx=10)

        birthday_flower_16 = tk.Button(scrollable_frame, image=self.img16, command=lambda: click("B016"))
        birthday_flower_16.grid(row=9, column=0, padx=10, pady=10)
        birthday_flower_16_label = tk.Label(scrollable_frame, text="B016 - RM 249.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_16_label.grid(row=10, column=0, padx=10)

        birthday_flower_17 = tk.Button(scrollable_frame, image=self.img17, command=lambda: click("B017"))
        birthday_flower_17.grid(row=9, column=3, padx=10, pady=10)
        birthday_flower_17_label = tk.Label(scrollable_frame, text="B017 - RM 199.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_17_label.grid(row=10, column=3, padx=10)

        birthday_flower_18 = tk.Button(scrollable_frame, image=self.img18, command=lambda: click("B018"))
        birthday_flower_18.grid(row=9, column=6, padx=10, pady=10)
        birthday_flower_18_label = tk.Label(scrollable_frame, text="B018 - RM 229.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_18_label.grid(row=10, column=6, padx=10)

        birthday_flower_19 = tk.Button(scrollable_frame, image=self.img19, command=lambda: click("B019"))
        birthday_flower_19.grid(row=9, column=9, padx=10, pady=10)
        birthday_flower_19_label = tk.Label(scrollable_frame, text="B019 - RM 299.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_19_label.grid(row=10, column=9, padx=10)

        birthday_flower_20 = tk.Button(scrollable_frame, image=self.img20, command=lambda: click("B020"))
        birthday_flower_20.grid(row=9, column=12, padx=10, pady=10)
        birthday_flower_20_label = tk.Label(scrollable_frame, text="B020 - RM 179.00", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_20_label.grid(row=10, column=12, padx=10)

        # Ensure that the images are kept in memory
        birthday_flower_1.image = self.img1a
        birthday_flower_2.image = self.img2
        birthday_flower_3.image = self.img3
        birthday_flower_4.image = self.img4
        birthday_flower_5.image = self.img5
        birthday_flower_6.image = self.img6
        birthday_flower_7.image = self.img7
        birthday_flower_8.image = self.img8
        birthday_flower_9.image = self.img9
        birthday_flower_10.image = self.img10
        birthday_flower_11.image = self.img11
        birthday_flower_12.image = self.img12
        birthday_flower_13.image = self.img13
        birthday_flower_14.image = self.img14
        birthday_flower_15.image = self.img15
        birthday_flower_16.image = self.img16
        birthday_flower_17.image = self.img17
        birthday_flower_18.image = self.img18
        birthday_flower_19.image = self.img19
        birthday_flower_20.image = self.img20

        # Update the scroll region of the canvas
        scrollable_frame.bind("<Configure>", lambda event, canvas=canvas: self.customer_ui.onFrameConfigure(canvas))
class graduationWindow:
    def __init__(self, root, customer_ui):
        self.root = root
        self.customer_ui = customer_ui

    def graduation_window(self):
        # Graduation label
        graduation_label = tk.Label(self.root, text="Graduation", font=("times new roman", 30), bg="pale violet red")
        graduation_label.pack(fill=tk.X, side=tk.TOP)

        # Create the main frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=1)

        # Create a canvas
        canvas = tk.Canvas(main_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Add a scrollbar to the canvas
        scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind_all("<MouseWheel>", self.customer_ui.mouse_scroll)

        # Create another frame inside the canvas
        scrollable_frame = tk.Frame(canvas)

        # Add that new frame to a window in the canvas
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        #Return to main menu
        returnToMain = tk.Button(self.root, text="<-", font=("times new roman", 20), command=self.customer_ui.returnToMain, fg="black", bg="yellow", compound=LEFT)
        returnToMain.place(x=10, y=10, height=50, width=50)

        # Graduation bouquet images
        self.img1 = tk.PhotoImage(file="images/graduation_bk838.gif")
        self.img2 = tk.PhotoImage(file="images/graduation_bq494.gif")
        self.img3 = tk.PhotoImage(file="images/graduation_bq568.gif")
        self.img4 = tk.PhotoImage(file="images/graduation_bq584.gif")
        self.img5 = tk.PhotoImage(file="images/graduation_bq684.gif")
        self.img6 = tk.PhotoImage(file="images/graduation_bq696.gif")
        self.img7 = tk.PhotoImage(file="images/graduation_bq795.gif")
        self.img8 = tk.PhotoImage(file="images/graduation_td472.gif")
        self.img9 = tk.PhotoImage(file="images/graduation_bq389.gif")
        self.img10 = tk.PhotoImage(file="images/graduation_bq446.gif")
        self.img11 = tk.PhotoImage(file="images/graduation_bq595.gif")
        self.img12 = tk.PhotoImage(file="images/graduation_bq593.gif")
        self.img13 = tk.PhotoImage(file="images/graduation_bq600.gif")
        self.img14 = tk.PhotoImage(file="images/graduation_bq655.gif")
        self.img15 = tk.PhotoImage(file="images/graduation_bq658.gif")
        self.img16 = tk.PhotoImage(file="images/graduation_bq673.gif")
        self.img17 = tk.PhotoImage(file="images/graduation_bq702.gif")
        self.img18 = tk.PhotoImage(file="images/graduation_bq725.gif")
        self.img19 = tk.PhotoImage(file="images/graduation_bq729.gif")
        self.img20 = tk.PhotoImage(file="images/graduation_bq804.gif")

        # Buttons for bouquets
        graduation_flower_1 = tk.Button(scrollable_frame, image=self.img1, command=lambda: click("G001"))
        graduation_flower_1.grid(row=0, column=0, padx=10, pady=10)
        graduation_flower_1_label = tk.Label(scrollable_frame, text="G001 - RM 359.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_1_label.grid(row=1, column=0, padx=10)
        
        graduation_flower_2 = tk.Button(scrollable_frame, image=self.img2, command=lambda: click("G002"))
        graduation_flower_2.grid(row=0, column=3, padx=10, pady=10)
        graduation_flower_2_label = tk.Label(scrollable_frame, text="G002 - RM 169.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_2_label.grid(row=1, column=3, padx=10)

        graduation_flower_3 = tk.Button(scrollable_frame, image=self.img3, command=lambda: click("G003"))
        graduation_flower_3.grid(row=0, column=6, padx=10, pady=10)
        graduation_flower_3_label = tk.Label(scrollable_frame, text="G003 - RM 229.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_3_label.grid(row=1, column=6, padx=10)

        graduation_flower_4 = tk.Button(scrollable_frame, image=self.img4, command=lambda: click("G004"))
        graduation_flower_4.grid(row=0, column=9, padx=10, pady=10)
        graduation_flower_4_label = tk.Label(scrollable_frame, text="G004 - RM 699.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_4_label.grid(row=1, column=9, padx=10)

        graduation_flower_5 = tk.Button(scrollable_frame, image=self.img5, command=lambda: click("G005"))
        graduation_flower_5.grid(row=0, column=12, padx=10, pady=10)
        graduation_flower_5_label = tk.Label(scrollable_frame, text="G005 - RM 69.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_5_label.grid(row=1, column=12, padx=10)

        graduation_flower_6 = tk.Button(scrollable_frame, image=self.img6, command=lambda: click("G006"))
        graduation_flower_6.grid(row=3, column=0, padx=10, pady=10)
        graduation_flower_6_label = tk.Label(scrollable_frame, text="G006 - RM 179.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_6_label.grid(row=4, column=0, padx=10)

        graduation_flower_7 = tk.Button(scrollable_frame, image=self.img7, command=lambda: click("G007"))
        graduation_flower_7.grid(row=3, column=3, padx=10, pady=10)
        graduation_flower_7_label = tk.Label(scrollable_frame, text="G007 - RM 269.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_7_label.grid(row=4, column=3, padx=10)

        graduation_flower_8 = tk.Button(scrollable_frame, image=self.img8, command=lambda: click("G008"))
        graduation_flower_8.grid(row=3, column=6, padx=10, pady=10)
        graduation_flower_8_label = tk.Label(scrollable_frame, text="G008 - RM 129.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_8_label.grid(row=4, column=6, padx=10)

        graduation_flower_9 = tk.Button(scrollable_frame, image=self.img9, command=lambda: click("G009"))
        graduation_flower_9.grid(row=3, column=9, padx=10, pady=10)
        graduation_flower_9_label = tk.Label(scrollable_frame, text="G009 - RM 479.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_9_label.grid(row=4, column=9, padx=10)

        graduation_flower_10 = tk.Button(scrollable_frame, image=self.img10, command=lambda: click("G010"))
        graduation_flower_10.grid(row=3, column=12, padx=10, pady=10)
        graduation_flower_10_label = tk.Label(scrollable_frame, text="G010 - RM 129.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_10_label.grid(row=4, column=12, padx=10)

        graduation_flower_11 = tk.Button(scrollable_frame, image=self.img11, command=lambda: click("G011"))
        graduation_flower_11.grid(row=6, column=0, padx=10, pady=10)
        graduation_flower_11_label = tk.Label(scrollable_frame, text="G011 - RM 249.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_11_label.grid(row=7, column=0, padx=10)

        graduation_flower_12 = tk.Button(scrollable_frame, image=self.img12, command=lambda: click("G012"))
        graduation_flower_12.grid(row=6, column=3, padx=10, pady=10)
        graduation_flower_12_label = tk.Label(scrollable_frame, text="G012 - RM 229.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_12_label.grid(row=7, column=3, padx=10)

        graduation_flower_13 = tk.Button(scrollable_frame, image=self.img13, command=lambda: click("G013"))
        graduation_flower_13.grid(row=6, column=6, padx=10, pady=10)
        graduation_flower_13_label = tk.Label(scrollable_frame, text="G013 - RM 469.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_13_label.grid(row=7, column=6, padx=10)

        graduation_flower_14 = tk.Button(scrollable_frame, image=self.img14, command=lambda: click("G014"))
        graduation_flower_14.grid(row=6, column=9, padx=10, pady=10)
        graduation_flower_14_label = tk.Label(scrollable_frame, text="G014 - RM 169.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_14_label.grid(row=7, column=9, padx=10)

        graduation_flower_15 = tk.Button(scrollable_frame, image=self.img15, command=lambda: click("G015"))
        graduation_flower_15.grid(row=6, column=12, padx=10, pady=10)
        graduation_flower_15_label = tk.Label(scrollable_frame, text="G015 - RM 179.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_15_label.grid(row=7, column=12, padx=10)

        graduation_flower_16 = tk.Button(scrollable_frame, image=self.img16, command=lambda: click("G016"))
        graduation_flower_16.grid(row=9, column=0, padx=10, pady=10)
        graduation_flower_16_label = tk.Label(scrollable_frame, text="G016 - RM 199.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_16_label.grid(row=10, column=0, padx=10)

        graduation_flower_17 = tk.Button(scrollable_frame, image=self.img17, command=lambda: click("G017"))
        graduation_flower_17.grid(row=9, column=3, padx=10, pady=10)
        graduation_flower_17_label = tk.Label(scrollable_frame, text="G017 - RM 229.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_17_label.grid(row=10, column=3, padx=10)

        graduation_flower_18 = tk.Button(scrollable_frame, image=self.img18, command=lambda: click("G018"))
        graduation_flower_18.grid(row=9, column=6, padx=10, pady=10)
        graduation_flower_18_label = tk.Label(scrollable_frame, text="G018 - RM 129.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_18_label.grid(row=10, column=6, padx=10)

        graduation_flower_19 = tk.Button(scrollable_frame, image=self.img19, command=lambda: click("G019"))
        graduation_flower_19.grid(row=9, column=9, padx=10, pady=10)
        graduation_flower_19_label = tk.Label(scrollable_frame, text="G019 - RM 199.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_19_label.grid(row=10, column=9, padx=10)

        graduation_flower_20 = tk.Button(scrollable_frame, image=self.img20, command=lambda: click("G020"))
        graduation_flower_20.grid(row=9, column=12, padx=10, pady=10)
        graduation_flower_20_label = tk.Label(scrollable_frame, text="G020 - RM 349.00", font=("times new roman", 20), fg="white", bg="pink")
        graduation_flower_20_label.grid(row=10, column=12, padx=10)

        # Ensure that the images are kept in memory
        graduation_flower_1.image = self.img1
        graduation_flower_2.image = self.img2
        graduation_flower_3.image = self.img3
        graduation_flower_4.image = self.img4
        graduation_flower_5.image = self.img5
        graduation_flower_6.image = self.img6
        graduation_flower_7.image = self.img7
        graduation_flower_8.image = self.img8
        graduation_flower_9.image = self.img9
        graduation_flower_10.image = self.img10
        graduation_flower_11.image = self.img11
        graduation_flower_12.image = self.img12
        graduation_flower_13.image = self.img13
        graduation_flower_14.image = self.img14
        graduation_flower_15.image = self.img15
        graduation_flower_16.image = self.img16
        graduation_flower_17.image = self.img17
        graduation_flower_18.image = self.img18
        graduation_flower_19.image = self.img19
        graduation_flower_20.image = self.img20

        # Update the scroll region of the canvas
        scrollable_frame.bind("<Configure>", lambda event, canvas=canvas: self.customer_ui.onFrameConfigure(canvas))

def checkoutfinal():
    purchaseitems = ""
    totalvalue=sum(purchaselistprice)
    for values in purchaselist:
        purchaseitems += values + "\n"
    purchase_confirmation = messagebox.askyesno("Items selected: \n", purchaseitems)
    if purchase_confirmation:
        messagebox.showinfo("Total amount of purchase", f"Your total purchase: RM {totalvalue:.2f}")
    else:
        purchaselist.clear()
        purchaselistprice.clear()
        messagebox.showinfo("Success", "Data cleared successfully!")

class RegistrationWindow(Customer):
    def __init__(self, root):
        super().__init__(None, None, None)
        self.customerDatabase = customerDatabase()
        self.root = root
    def input_info(self):
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

    def register_info(self):
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        email = self.email_entry.get()
        if name in [customer.name for customer in self.customerDatabase.customer_info] or contact in [customer.contact for customer in self.customerDatabase.customer_info] or email in [customer.email for customer in self.customerDatabase.customer_info]:
            messagebox.showinfo("","Name already recorded.")
        else:
            new_customer = Customer(name, contact, email)
            self.customerDatabase.customer_info.append(new_customer)
            self.customerDatabase.saveCustomerInfo()
            messagebox.showinfo("Registration Successful", f"Thank you {name} for registering.")
            self.register_popUp.destroy()
            
class customer_UI:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.title("Kedai Bunga | Developed by Kawabunga")
        self.root.config(bg="white")
        self.birthdayWindow = birthdayWindow(root, self)
        self.funeralWindow = funeralWindow(root, self)
        self.graduationWindow = graduationWindow(root, self)
        self.registrationWindow = RegistrationWindow(root)
        self.createMainMenu()

#====Main Menu====
    def createMainMenu(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Kedai Bunga", font=("times new roman", 40, "bold"), fg="white", bg="pink")
        self.title_label.place(x=0, y=0, relwidth=1, height=70)

        # Log Out Button (myb change to contact smth like that)
        self.logout_button = tk.Button(self.root, text="Log Out", font=("times new roman", 15, "bold"), bg="yellow", compound=tk.CENTER, cursor="hand2")
        self.logout_button.place(x=1770, y=0, height=70, width=150)

        # Clock Label
        current_date = datetime.now().date()
        current_time = datetime.now().time()
        self.clock_label = tk.Label(self.root, text=f"{current_date} | {current_time.strftime('%H:%M:%S')}", font=("times new roman", 20), bg="pale violet red")
        self.clock_label.place(x=0, y=70, relwidth=1, height=30)

        # Promotion panel
        self.promotion_label = tk.Label(self.root, text="Promotion!!", font=("times new roman", 50), bg="hot pink")
        self.promotion_label.place(x=200, y=102, relwidth=1, height=300)

        # Left Menu
        left_menu = tk.Frame(self.root, bd=2, relief=tk.RIDGE, bg="white")
        left_menu.place(x=0, y=102, width=200, height=1565)
        menu_label = tk.Label(left_menu, text="Menu", font=("times new roman", 20), bg="pink")
        menu_label.pack(side=tk.TOP, fill=tk.X)
        img_menu = PhotoImage(file = "images/png.gif")
        img_menu_label = tk.Label(left_menu, image=img_menu)
        img_menu_label.pack(side=TOP, fill=tk.X)

        # Buttons in Left Menu
        order_button = tk.Button(left_menu, text="\nOrder\n", font=("times new roman", 20), bg="white", bd=3, cursor="hand2")
        order_button.pack(side=tk.TOP, fill=tk.X)
        register_button = tk.Button(left_menu, text="\nRegister\n", command=self.registrationWindow.input_info, font=("times new roman", 20), bg="white", bd=3, cursor="hand2")
        register_button.pack(side=tk.TOP, fill=tk.X)
        promotion_button = tk.Button(left_menu, text="\nPromotion\n", font=("times new roman", 20), bg="white", bd=3, cursor="hand2")
        promotion_button.pack(side=tk.TOP, fill=tk.X)
        admin_button = tk.Button(left_menu, text="\nSettings\n", command=self.open_admin_UI, font=("times new roman", 20), bg="white", bd=3, cursor="hand2")
        admin_button.pack(side=tk.TOP, fill=tk.X)

        #Add images of categories here (refer to birthday window)
        # Birthday logo
        self.img1 = tk.PhotoImage(file="images/birthdaylogo.gif")

        birthday = tk.Button(self.root, image=self.img1, command=self.birthdayWindow.birthday_window)
        birthday.place(x=300, y=420, height=300, width=300)
        birthday_label = tk.Label(self.root, text="Birthday", font=("times new roman", 20), fg="white", bg="pink")
        birthday_label.place(x=300, y=720, height=30, width=300)

        # Funeral logo 
        self.img2 = tk.PhotoImage(file="images/funerallogo.gif")

        funeral = tk.Button(self.root, image=self.img2, command=self.funeralWindow.funeral_window)
        funeral.place(x=700, y=420, height=300, width=300)
        funeral_label = tk.Label(self.root, text="Funeral", font=("times new roman", 20), fg="white", bg="pink")
        funeral_label.place(x=700, y=720, height=30, width=300)

        # Graduation logo 
        self.img3 = tk.PhotoImage(file="images/graduationlogo.gif")

        graduation = tk.Button(self.root, image=self.img3, command=self.graduationWindow.graduation_window)
        graduation.place(x=1100, y=420, height=300, width=300)
        graduation_label = tk.Label(self.root, text="Graduation", font=("times new roman", 20), fg="white", bg="pink")
        graduation_label.place(x=1100, y=720, height=30, width=300)

        checkout= tk.Button(self.root, text="Checkout", font=("times new roman", 10), fg="white", bg="grey", command=checkoutfinal)
        checkout.place(x=1420, y=600, height=90, width=90)

        # Footer
        contact_label = tk.Label(self.root, text="For further inquiries, please contact 019-999-9999", font=("times new roman", 20), fg="white", bg="pale violet red")
        contact_label.pack(side=tk.BOTTOM, fill=tk.X)
        pass

#====Admin UI====
    def open_admin_UI(self):
        subprocess.Popen(["python", "main_admin.py"])
        exit()

#====Call this to return to Main Menu====
    def returnToMain(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.createMainMenu()

    def onFrameConfigure(self, canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

    def mouse_scroll(self, event):
        canvas = event.widget
        canvas.yview_scroll(-1 * (event.delta // 120), "units")

root = tk.Tk()
app = customer_UI(root)
root.mainloop()