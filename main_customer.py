import subprocess
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime

class birthdayWindow:
    def __init__(self, root, customer_ui):
        self.root = root
        self.customer_ui = customer_ui

    def birthday_window(self):
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

        self.birthday_label = tk.Label(self.root, text="Birthday", font=("times new roman", 40, "bold"), fg="white", bg="pink")
        self.birthday_label.place(x=0, y=0, relwidth=1, height=70)

        #Return to main menu
        returnToMain = tk.Button(self.root, text="<-", font=("times new roman", 20), command=self.customer_ui.returnToMain, fg="black", bg="yellow", compound=LEFT)
        returnToMain.place(x=10, y=10, height=50, width=50)

        # Load the birthday bouquet images
        self.img1 = tk.PhotoImage(file="images/birthday_img1.gif")
        self.img2 = tk.PhotoImage(file="images/birthday_img2.gif")

        # Create buttons for the bouquets
        birthday_flower_1 = tk.Button(scrollable_frame, image=self.img1)
        birthday_flower_1.grid(row=0, column=0, padx=10, pady=10)
        birthday_flower_1_label = tk.Label(scrollable_frame, text="Pilihan 1", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_1_label.grid(row=1, column=0, padx=10)

        birthday_flower_2 = tk.Button(scrollable_frame, image=self.img2)
        birthday_flower_2.grid(row=3, column=0, padx=10, pady=10)
        birthday_flower_2_label = tk.Label(scrollable_frame, text="Pilihan 2", font=("times new roman", 20), fg="white", bg="pink")
        birthday_flower_2_label.grid(row=4, column=0, padx=10)

        # Ensure that the images are kept in memory
        birthday_flower_1.image = self.img1
        birthday_flower_2.image = self.img2

        # Update the scroll region of the canvas
        scrollable_frame.bind("<Configure>", lambda event, canvas=canvas: self.customer_ui.onFrameConfigure(canvas))

class funeralWindow:
    def __init__(self) -> None:
        pass

class graduationWindow:
    def __init__(self) -> None:
        pass

class customer_UI:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.title("Kedai Bunga | Developed by Kawabunga")
        self.root.config(bg="white")
        self.birthdayWindow = birthdayWindow(root, self)
        self.funeralWindow = funeralWindow()
        self.graduationWindow = graduationWindow()
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
        category_button = tk.Button(left_menu, text="\nCategory\n", font=("times new roman", 20), bg="white", bd=3, cursor="hand2")
        category_button.pack(side=tk.TOP, fill=tk.X)
        promotion_button = tk.Button(left_menu, text="\nPromotion\n", font=("times new roman", 20), bg="white", bd=3, cursor="hand2")
        promotion_button.pack(side=tk.TOP, fill=tk.X)
        admin_button = tk.Button(left_menu, text="\nSettings\n", command=self.open_admin_UI, font=("times new roman", 20), bg="white", bd=3, cursor="hand2")
        admin_button.pack(side=tk.TOP, fill=tk.X)

        #Add images of categories here (refer to birhtday window)

        #Categories buttons
        self.birthday_button = tk.Button(root, text="Birthday", command=self.birthdayWindow.birthday_window, bg="pink", fg="white", font=("times new roman", 30), cursor="hand2")
        self.birthday_button.place(x=300, y=420, height=300, width=300)
        self.funeral_button = tk.Button(root, text="Funeral", command=None, bg="pink", fg="white", font=("times new roman", 30), cursor="hand2")
        self.funeral_button.place(x=700, y=420, height=300, width=300)
        self.graduation_button = tk.Button(root, text="",command=None, bg="pink", fg="white", font=("times new roman", 30), cursor="hand2")
        self.graduation_button.place(x=1100, y=420, height=300, width=300)

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
